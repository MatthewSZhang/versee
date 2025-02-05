"""Streamlit app"""

import click
import streamlit as st

from ._content import _get_content
from ._data import _extract_bible
from ._ref import _parse_reference


@click.command()
@click.option("--version", type=str, default="cmn-cu89s")
def web(version):
    bible = _extract_bible(version)
    reference = st.text_input("Bible Reference", placeholder="gen 1:10-2:15")
    if reference:
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
        st.markdown("\n".join(content))
