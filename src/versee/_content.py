"""Process content"""

import pandas as pd


def _format_verses(
    content: pd.DataFrame, start_verse: int = 1, end_verse: int | None = None
):
    if end_verse is None:
        end_verse = content["verse"].str.split("-").explode().astype(int).max()
    formatted_content = []
    for verse_num in range(start_verse, end_verse + 1):
        verse = content[content["verse"] == str(verse_num)]
        if verse.empty:
            verse = content[content["verse"].str.endswith(f"-{verse_num}")]
        if verse.empty:
            verse = content[content["verse"].str.startswith(f"{verse_num}-")]
            if not verse.empty and verse_num != end_verse:
                formatted_content.append(f"{verse_num}. " + "EMPTY")
                continue
        if verse.empty:
            raise ValueError(
                f"Book {content.iloc[0]["book"]}, Chapter {content.iloc[0]["chapter"]},"
                f"Verse {verse_num} not found."
            )
        formatted_content.append(f"{verse_num}. " + verse.iloc[0]["text"])
    return formatted_content


def _get_content(
    bible: pd.DataFrame,
    book: str,
    start_chapter: int,
    start_verse: int | None = None,
    end_chapter: int | None = None,
    end_verse: int | None = None,
):
    """Get Bible content from web pages"""
    if start_verse is None:
        start_verse = 1
    if end_chapter is None:
        end_chapter = start_chapter

    book_content = bible[bible["book"] == book]
    formatted_content = []
    for i in range(start_chapter, end_chapter + 1):
        chapter_content = book_content[book_content["chapter"] == str(i)]
        formatted_content.append(f"## {book.upper()} {i}")
        if i == start_chapter:
            _start_verse = start_verse
        else:
            _start_verse = 1
        if i == end_chapter:
            _end_verse = end_verse
        else:
            _end_verse = None
        formatted_content += _format_verses(chapter_content, _start_verse, _end_verse)

    return formatted_content
