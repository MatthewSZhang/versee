import zipfile
from io import BytesIO

import click
from lxml import etree


@click.command()
@click.argument("book", type=str)
@click.option("--epub_path", type=str, default="versions/cmn-cu89s.epub")
def _print_etree(book: str, epub_path: str):
    """Print raw content of a book"""
    with zipfile.ZipFile(epub_path, "r") as epub:
        file_list = epub.namelist()
        xhtml_file = [f for f in file_list if f.endswith(f"{book.upper()}.xhtml")]
        if xhtml_file:
            with epub.open(xhtml_file[0]) as book_file:
                book_content = book_file.read()
            tree = etree.parse(BytesIO(book_content))
            print(etree.tostring(tree, pretty_print=True, encoding="unicode"))
