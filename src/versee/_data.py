"""Download epub files from ebible.org"""

import os
import zipfile
from io import BytesIO

import pandas as pd
import requests
from lxml import etree

from ._ref import BOOKS

NAMESPACES = "http://www.w3.org/1999/xhtml"
STRIP = " \t\n\r¶"


def _download_epub(version: str, save_path: str):
    url = f"https://ebible.org/epub/{version}.epub"
    # Create the versions directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # Download the file
    response = requests.get(url, timeout=200)
    with open(save_path, "wb") as file:
        file.write(response.content)


# New: iterate text in correct document order and mark verse boundaries
def _iter_doc_events(elem):
    skip_classes = {"noteref", "r", "s", "sp"}
    span_tag = f"{{{NAMESPACES}}}span"

    def is_verse(n):
        return n.tag == span_tag and n.attrib.get("class", "") == "verse"

    def walk(n):
        if n.text and n.attrib.get("class", "") not in skip_classes and not is_verse(n):
            yield ("text", n.text)
        for child in n:
            if is_verse(child):
                num = (child.text or "").strip()
                if num:
                    yield ("verse", num)
            elif child.attrib.get("class", "") not in skip_classes:
                yield from walk(child)
            # Always include child.tail in order
            if child.tail:
                yield ("text", child.tail)

    yield from walk(elem)


def _extract_chapters(tree):
    # Initialize variables
    chapters = {}
    verses = {}
    current_verse_num = None
    current_chapter_num = None

    # Iterate over all elements
    for elem in tree.iter(f"{{{NAMESPACES}}}div"):
        if "psalmlabel" == elem.attrib.get("class", ""):
            # Found a chapter label
            if current_chapter_num is None:
                current_chapter_num = elem.text.strip()
            else:
                chapters[current_chapter_num] = verses
                current_chapter_num = elem.text.strip()
                verses = {}
                current_verse_num = None
        elif "footnote" == elem.attrib.get("class", ""):
            # End of a book
            chapters[current_chapter_num] = verses
        elif "main" == elem.attrib.get("class", ""):
            continue
        else:
            # Check if the <div> contains a <span> with class "verse"
            verse_span = elem.find(f".//{{{NAMESPACES}}}span[@class='verse']")
            if verse_span is not None:
                # Collect text in proper document order
                for kind, val in _iter_doc_events(elem):
                    if kind == "verse":
                        current_verse_num = val  # start a new verse
                        verses[current_verse_num] = []
                    elif kind == "text" and current_verse_num:
                        verses[current_verse_num].append(val.strip(STRIP))
            elif current_verse_num:
                # Continuation of the same verse: collect text in order
                for kind, val in _iter_doc_events(elem):
                    if kind == "text":
                        verses[current_verse_num].append(val.strip(STRIP))
    return chapters


def _to_parquet(epub_path: str, parquet_path: str):
    """Convert the downloaded EPUB file to a parquet file."""
    # Step 1: Open the EPUB file as a ZIP archive
    with zipfile.ZipFile(epub_path, "r") as epub:
        # Step 2: Find the main content files
        file_list = epub.namelist()

        # Step 3: Locate XHTML content files
        books = pd.DataFrame(
            {
                "book": [],
                "chapter": [],
                "verse": [],
                "text": [],
            }
        )
        for file in BOOKS:
            xhtml_file = [f for f in file_list if f.endswith(f"{file.upper()}.xhtml")]
            if xhtml_file:
                # Extract and parse the first XHTML file
                with epub.open(xhtml_file[0]) as book_file:
                    book_content = book_file.read()

                # Step 4: Parse with lxml
                tree = etree.parse(BytesIO(book_content))
                chapters = _extract_chapters(tree)

                for chapter_num, verses in chapters.items():
                    for verse_num, text in verses.items():
                        books = pd.concat(
                            [
                                books,
                                pd.DataFrame(
                                    {
                                        "book": [file],
                                        "chapter": [chapter_num],
                                        "verse": [verse_num],
                                        "text": ["".join(text).strip(STRIP)],
                                    }
                                ),
                            ],
                            ignore_index=True,
                        )
    os.makedirs(os.path.dirname(parquet_path), exist_ok=True)
    books.to_parquet(parquet_path, engine="pyarrow")


def _extract_bible(version: str):
    """Extract Bible text from the EPUB file."""
    epub_path = f"versions/{version}.epub"
    parquet_path = f"data/{version}.parquet"
    # Check if the file already exists
    if not os.path.exists(epub_path):
        # Download the file
        _download_epub(version, epub_path)
        print(f"Epub file downloaded and saved to {epub_path}")
    else:
        print(f"Epub file already exists at {epub_path}")

    if not os.path.exists(parquet_path):
        # Convert to parquet
        _to_parquet(epub_path, parquet_path)
        print(f"Parquet file created and saved to {parquet_path}")
    else:
        print(f"Parquet file already exists at {parquet_path}")
    return pd.read_parquet(parquet_path)
