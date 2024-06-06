from pathlib import Path
from typing import List

import pytest

from pyconverters_grobid.grobid import GrobidConverter, GrobidParameters, InputFormat
from pymultirole_plugins.v1.schema import Document, DocumentList
from starlette.datastructures import UploadFile


def test_grobid_pdf():
    converter = GrobidConverter()
    parameters = GrobidParameters(sentences=True, citations=True)
    testdir = Path(__file__).parent
    source = Path(testdir, "data/PMC1636350.pdf")
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(
            UploadFile(source.name, fin, "application/pdf"), parameters
        )
    assert len(docs) == 1
    assert docs[0].identifier
    assert docs[0].text
    assert docs[0].title
    assert "TITLE" in docs[0].boundaries
    assert docs[0].annotations
    assert docs[0].sentences
    assert len(docs[0].annotations[0].terms) == 1
    json_file = source.with_suffix(".json")
    dl = DocumentList(__root__=docs)
    with json_file.open("w") as fout:
        print(dl.json(exclude_none=True, exclude_unset=True, indent=2), file=fout)


def test_grobid_pdf2():
    converter = GrobidConverter()
    parameters = GrobidParameters(sentences=True, citations=True, figures=True,
                                  header_regex="(?i)materials .* methods")
    testdir = Path(__file__).parent
    source = Path(testdir, "data/PMC1636350.pdf")
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(
            UploadFile(source.name, fin, "application/pdf"), parameters
        )
    assert len(docs) == 1
    assert docs[0].identifier
    assert docs[0].text.startswith("MATERIALS")
    assert docs[0].title
    assert "MATERIALS AND METHODS" in docs[0].boundaries
    assert docs[0].annotations
    assert docs[0].sentences
    assert len(docs[0].annotations[0].terms) == 1
    json_file = source.with_suffix(".json")
    dl = DocumentList(__root__=docs)
    with json_file.open("w") as fout:
        print(dl.json(exclude_none=True, exclude_unset=True, indent=2), file=fout)


def test_grobid_list():
    converter = GrobidConverter()
    parameters = GrobidParameters(
        input_format=InputFormat.URL_List, sentences=True, citations=True, extract_abstract=True
    )
    testdir = Path(__file__).parent
    source = Path(testdir, "data/listpdfs.txt")
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(
            UploadFile(source.name, fin, "text/plain"), parameters
        )
    assert len(docs) == 2
    docs[0].altTexts[0].name == 'abstract'


@pytest.mark.skip(reason="Not a test")
def test_grobid_bilit():
    converter = GrobidConverter()
    parameters = GrobidParameters(sentences=True, citations=True, extract_abstract=True)
    testdir = Path(__file__).parent
    source = Path(testdir, "data/65d35c83db7a39f879a6866c_P23-04063.pdf")
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(
            UploadFile(source.name, fin, "application/pdf"), parameters
        )
    assert len(docs) == 1
    assert docs[0].identifier
    assert docs[0].text
    assert docs[0].title
    assert "TITLE" in docs[0].boundaries
    assert docs[0].annotations
    assert docs[0].sentences
    assert len(docs[0].annotations[0].terms) == 1
    json_file = source.with_suffix(".json")
    dl = DocumentList(__root__=docs)
    with json_file.open("w") as fout:
        print(dl.json(exclude_none=True, exclude_unset=True, indent=2), file=fout)
