# versee

`versee` is a Python package that scrapes Bible content from [eBible.org](https://ebible.org/).
It mainly has following features:

1. Output the selected Bible content to a (Markdown) file (for printing).
2. Display the selected Bible content in a web page.

# How to use it

[uv](https://docs.astral.sh/uv/getting-started/installation/) should be installed first.

1. Export to file

```shell
uv run file "gen 1" --filepath output.md
```

The default version is `cmn-cu89s`.
Version can be changed by running

```shell
uv run file "gen 1" --version eng-kjv2006 --filepath output.md
```


2. Web App

```shell
uv run web 
```
Use `Ctrl + C` to exit the application.

The default version is `cmn-cu89s`.
Version can be changed by running

```shell
uv run web --version eng-kjv2006
```

# Bible reference

We support the following Bible references:

1. gen 2 (Genesis Chapter 2)
2. gen 2:3 (Genesis Chapter 2 Verse 3)
3. gen 2:3- (Genesis Chapter 2 Verse 3 to the end of the chapter)
4. gen 2:3-5 (Genesis Chapter 2 Verse 3 to Verse 5)
5. gen 2:3-4:- (Genesis Chapter 2 Verse 3 to the end of Chapter 4)
6. gen 2:3-4:5 (Genesis Chapter 2 Verse 3 to Chapter 4 Verse 5)
7. gen 1-3 (Genesis Chapter 2 Verse 3 to Chapter 4 Verse 5)

## Multiple references

We also support multiple references like:

`gen 2:13-15; 3:16; exo 2; 3:10-; psa 1-3; 76:7-77:-; rev 21:20-22:10, 17-21; jhn 10:10`

1. Semicolon `;` is used for disconnected verses in different chapters and books
2. Comma `,` is used for disconnected verses in the same chapter

# Code of Bible books

| Code | Book          | 中文          |
| ---- | ------------- | ------------ |
| gen  | Genesis       | 创世记       |
| exo  | Exodus        | 出埃及记     |
| lev  | Leviticus     | 利未记       |
| num  | Numbers       | 民数记       |
| deu  | Deuteronomy   | 申命记       |
| jos  | Joshua        | 约书亚记     |
| jdg  | Judges        | 士师记       |
| rut  | Ruth          | 路得记       |
| 1sa  | 1 Samuel      | 撒母耳记上   |
| 2sa  | 2 Samuel      | 撒母耳记下   |
| 1ki  | 1 Kings       | 列王记上     |
| 2ki  | 2 Kings       | 列王记下     |
| 1ch  | 1 Chronicles  | 历代志上     |
| 2ch  | 2 Chronicles  | 历代志下     |
| ezr  | Ezra          | 以斯拉记     |
| neh  | Nehemiah      | 尼希米记     |
| est  | Esther        | 以斯帖记     |
| job  | Job           | 约伯记       |
| psa  | Psalms        | 诗篇         |
| pro  | Proverbs      | 箴言         |
| ecc  | Ecclesiastes  | 传道书       |
| sng  | Song of Solomon| 雅歌        |
| isa  | Isaiah        | 以赛亚书     |
| jer  | Jeremiah      | 耶利米书     |
| lam  | Lamentations  | 耶利米哀歌   |
| ezk  | Ezekiel       | 以西结书     |
| dan  | Daniel        | 但以理书     |
| hos  | Hosea         | 何西阿书     |
| jol  | Joel          | 约珥书       |
| amo  | Amos          | 阿摩司书     |
| oba  | Obadiah       | 俄巴底亚书   |
| jon  | Jonah         | 约拿书       |
| mic  | Micah         | 弥迦书       |
| nam  | Nahum         | 那鸿书       |
| hab  | Habakkuk      | 哈巴谷书     |
| zep  | Zephaniah     | 西番雅书     |
| hag  | Haggai        | 哈该书       |
| zec  | Zechariah     | 撒迦利亚书   |
| mal  | Malachi       | 玛拉基书     |
| mat  | Matthew       | 马太福音     |
| mrk  | Mark          | 马可福音     |
| luk  | Luke          | 路加福音     |
| jhn  | John          | 约翰福音     |
| act  | Acts          | 使徒行传     |
| rom  | Romans        | 罗马书       |
| 1co  | 1 Corinthians | 哥林多前书   |
| 2co  | 2 Corinthians | 哥林多后书   |
| gal  | Galatians     | 加拉太书     |
| eph  | Ephesians     | 以弗所书     |
| php  | Philippians   | 腓立比书     |
| col  | Colossians    | 歌罗西书     |
| 1th  | 1 Thessalonians| 帖撒罗尼迦前书|
| 2th  | 2 Thessalonians| 帖撒罗尼迦后书|
| 1ti  | 1 Timothy     | 提摩太前书   |
| 2ti  | 2 Timothy     | 提摩太后书   |
| tit  | Titus         | 提多书       |
| mon  | Philemon      | 腓利门书     |
| heb  | Hebrews       | 希伯来书     |
| jas  | James         | 雅各书       |
| 1pe  | 1 Peter       | 彼得前书     |
| 2pe  | 2 Peter       | 彼得后书     |
| 1jn  | 1 John        | 约翰一书     |
| 2jn  | 2 John        | 约翰二书     |
| 3jn  | 3 John        | 约翰三书     |
| jud  | Jude          | 犹大书       |
| rev  | Revelation    | 启示录       |

# Versions

`versee` supports the Bible versions on [eBible.org](https://ebible.org/Scriptures/).
