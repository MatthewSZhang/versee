"""Reference parsing utilities"""

import re

BOOKS = {
    "gen": "Genesis",
    "exo": "Exodus",
    "lev": "Leviticus",
    "num": "Numbers",
    "deu": "Deuteronomy",
    "jos": "Joshua",
    "jdg": "Judges",
    "rut": "Ruth",
    "1sa": "1 Samuel",
    "2sa": "2 Samuel",
    "1ki": "1 Kings",
    "2ki": "2 Kings",
    "1ch": "1 Chronicles",
    "2ch": "2 Chronicles",
    "ezr": "Ezra",
    "neh": "Nehemiah",
    "est": "Esther",
    "job": "Job",
    "psa": "Psalms",
    "pro": "Proverbs",
    "ecc": "Ecclesiastes",
    "sng": "Song of Solomon",
    "isa": "Isaiah",
    "jer": "Jeremiah",
    "lam": "Lamentations",
    "ezk": "Ezekiel",
    "dan": "Daniel",
    "hos": "Hosea",
    "jol": "Joel",
    "amo": "Amos",
    "oba": "Obadiah",
    "jon": "Jonah",
    "mic": "Micah",
    "nam": "Nahum",
    "hab": "Habakkuk",
    "zep": "Zephaniah",
    "hag": "Haggai",
    "zec": "Zechariah",
    "mal": "Malachi",
    "mat": "Matthew",
    "mrk": "Mark",
    "luk": "Luke",
    "jhn": "John",
    "act": "Acts",
    "rom": "Romans",
    "1co": "1 Corinthians",
    "2co": "2 Corinthians",
    "gal": "Galatians",
    "eph": "Ephesians",
    "php": "Philippians",
    "col": "Colossians",
    "1th": "1 Thessalonians",
    "2th": "2 Thessalonians",
    "1ti": "1 Timothy",
    "2ti": "2 Timothy",
    "tit": "Titus",
    "mon": "Philemon",
    "heb": "Hebrews",
    "jas": "James",
    "1pe": "1 Peter",
    "2pe": "2 Peter",
    "1jn": "1 John",
    "2jn": "2 John",
    "3jn": "3 John",
    "jud": "Jude",
    "rev": "Revelation",
}


def _parse_verse(reference):
    pattern = re.compile(r"(\d+)(?::(\d+))?(?:-(\d+)?(?::(\d+))?)?")
    match = pattern.match(reference)

    if not match:
        raise ValueError(f"Invalid reference format: {reference}")

    start_chapter = int(match.group(1))
    start_verse = int(match.group(2)) if match.group(2) else 1
    end_chapter = int(match.group(3)) if match.group(3) else start_chapter
    end_verse = (
        int(match.group(4))
        if match.group(4)
        else (
            None if reference.endswith("-") else start_verse if match.group(2) else None
        )
    )
    if (
        match.group(3)
        and match.group(2)
        and not match.group(4)
        and not reference.endswith("-")
    ):
        end_chapter = start_chapter
        end_verse = int(match.group(3))
    return start_chapter, start_verse, end_chapter, end_verse


def _parse_reference(reference):
    references = reference.split(";")
    parsed_references = []

    current_book = None
    for ref in references:
        ref = ref.strip()
        if ref[:3].isalpha():
            book, verses = ref.split(" ", 1)
            current_book = book.lower()
            if current_book not in BOOKS:
                raise ValueError(f"Unknown book: {book}")
        else:
            verses = ref

        prefix_chapter = ""
        for verse in verses.split(","):
            verse = verse.strip()
            verse = prefix_chapter + verse
            start_chapter, start_verse, end_chapter, end_verse = _parse_verse(verse)
            prefix_chapter = f"{end_chapter}:"
            parsed_references.append(
                (current_book, start_chapter, start_verse, end_chapter, end_verse)
            )

    return parsed_references
