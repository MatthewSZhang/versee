"""Test Data"""

from versee._content import _get_content
from versee._data import _extract_bible
from versee._ref import _parse_reference


def test_r():
    """Test r (cross-reference) class handling"""
    reference = "jhn 11:44"
    version = "cmn-cu89s"
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
    assert "（太26·1—5；可14·1—2；路22·1—2）" not in content[-1]
