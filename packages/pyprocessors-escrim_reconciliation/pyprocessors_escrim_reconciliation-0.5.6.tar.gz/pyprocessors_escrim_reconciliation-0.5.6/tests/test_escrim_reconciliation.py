import json
from pathlib import Path

from dirty_equals import Contains, IsPartialDict
from pymultirole_plugins.v1.schema import Document, Annotation, DocumentList
from pytest_check import check

from pyprocessors_escrim_reconciliation.escrim_reconciliation import (
    EscrimReconciliationProcessor,
    EscrimReconciliationParameters,
)


def test_model():
    model = EscrimReconciliationProcessor.get_model()
    model_class = model.construct().__class__
    assert model_class == EscrimReconciliationParameters


def by_lexicon(a: Annotation):
    if a.terms:
        return a.terms[0].lexicon
    else:
        return ""


def by_label(a: Annotation):
    return a.labelName or a.label


def by_linking(a: Annotation):
    if a.terms:
        links = sorted({t.lexicon.split("_")[0] for t in a.terms})
        return "+".join(links)
    else:
        return "candidate"


def test_escrim_fr():
    testdir = Path(__file__).parent
    source = Path(testdir, "data/escrim_meta-document-test.json")
    with source.open("r") as fin:
        doc = json.load(fin)
        original_doc = Document(**doc)
        processor = EscrimReconciliationProcessor()
        parameters = EscrimReconciliationParameters(person_labels=["personne"],
                                                    geo_labels=["lieu", "loc_org"],
                                                    meta_labels=["meta_equipement", "meta_site"],
                                                    resolve_lastnames=True)
        docs = processor.process([original_doc.copy(deep=True)], parameters)
        consolidated: Document = docs[0]
        assert len(original_doc.annotations) > len(consolidated.annotations)
        result = Path(testdir, "data/escrim_meta-document_conso.json")
        with result.open("w") as fout:
            json.dump(consolidated.dict(), fout, indent=2)


def get_bug_documents(bug):
    datadir = Path(__file__).parent / "data"
    docs = {}
    for bug_file in datadir.glob(f"{bug}*.json"):
        with bug_file.open("r") as fin:
            doc = json.load(fin)
            doc['identifier'] = bug_file.stem
            docs[bug_file.stem] = Document(**doc)
    myKeys = list(docs.keys())
    myKeys.sort()
    sorted_docs = {i: docs[i] for i in myKeys}
    return list(sorted_docs.values())


def write_bug_result(bug, docs, type):
    datadir = Path(__file__).parent / "data"
    result = Path(datadir, f"result_{bug}_{type}.json")
    dl = DocumentList(__root__=docs)
    with result.open("w") as fout:
        print(dl.json(exclude_none=True, exclude_unset=True, indent=2), file=fout)


# [ESCRIM] "Clemenceau" is not linked to the lexicon
def test_SHERPA_XXX1():
    docs = get_bug_documents("SHERPA-XXX1")
    processor = EscrimReconciliationProcessor()
    parameters = EscrimReconciliationParameters(person_labels=["personne"],
                                                geo_labels=["lieu", "loc_org"],
                                                meta_labels=["meta_equipement", "meta_site"],
                                                resolve_lastnames=True)
    docs = processor.process(docs, parameters)
    write_bug_result("SHERPA-1735", docs, parameters.type)
    doc0 = docs[0]
    clemenceau = next(a.dict(exclude_none=True, exclude_unset=True) for a in doc0.annotations if
                      a.text == "Clemenceau")
    with check:
        assert clemenceau == IsPartialDict(label="Nom d'équipement", text="Clemenceau",
                                           terms=Contains(
                                               IsPartialDict(lexicon="equipment_classes")
                                           ))

    # super_etendard = next(a.dict(exclude_none=True, exclude_unset=True) for a in doc0.annotations if
    #                     a.text == 'Super-Étendard')
    # with check:
    #     assert super_etendard == IsPartialDict(label="Classe d'équipement", text='Super-Étendard',
    #                                          terms=Contains(
    #                                              IsPartialDict(lexicon="equipment_classes")
    #                                         ))
