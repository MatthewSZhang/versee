"""Write to a Markdown file"""

import click

from ._content import _get_content
from ._data import _extract_bible
from ._ref import _parse_reference


@click.command()
@click.argument("reference", type=str)
@click.option("--version", type=str, default="cmn-cu89s")
@click.option("--filepath", type=str, default="output.md")
def write_file(
    reference: str,
    version: str = "cmn-cu89s",
    filepath: str = "output.md",
):
    """Write Bible content to a file"""
    bible = _extract_bible(version)
    parsed = _parse_reference(reference)
    content = []
    for ref in parsed:
        content += _get_content(
            bible,
            book=ref[0],
            start_chapter=ref[1],
            start_verse=ref[2],
            end_chapter=ref[3],
            end_verse=ref[4],
        )

    # Write the list of strings to the Markdown file
    with open(filepath, "w", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")
