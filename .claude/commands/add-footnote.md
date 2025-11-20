---
description: Add section word footnote to a specific word in a verse
---

You are helping to add section word footnotes to Isaiah chapter tex files.

## Input Format:
The user will provide:
1. Chapter and verse (e.g., "19:1" or "Isaiah 19:1")
2. The word to add the footnote to
3. The footnote text

Example: "19:1 tremble - 'to quiver' — like the doorposts in ch 6 or King Ahaz of ch 7"

## Process:
1. Parse the user's input to extract:
   - Chapter number
   - Verse number (including letter suffixes like "1b" if present)
   - The word to footnote
   - The footnote text
2. Read the appropriate chapter file from `/Users/luke.schmidt/code/isaiah/chapters/isaiah-{chapter}/isaiah-{chapter}.tex`
3. Find the specific verse in the file
4. Locate the word within that verse
5. Wrap the word with `\sectionwordfootnote{word}{footnote text}`
6. Make the edit

## Important Notes:
- Use `\sectionwordfootnote` NOT `\sectionword`
- The word may already have other LaTeX commands around it (like `\highlightpurple{}`)
- Preserve all existing formatting and highlights
- If the word appears multiple times in the verse, use context to determine which instance to footnote (or ask the user)
- Verse numbers in the tex file are marked with `\versenum{X}`
- Verses may have letter suffixes (1a, 1b, 1c, etc.) in chiastic structures

## Example:
Input: "19:1 tremble - 'to quiver' — like the doorposts in ch 6 or King Ahaz of ch 7"

Before:
```latex
\versenum{1b} and the \highlightpurple{idols} of \highlightyellow{Egypt} will tremble at his presence,
```

After:
```latex
\versenum{1b} and the \highlightpurple{idols} of \highlightyellow{Egypt} will \sectionwordfootnote{tremble}{'to quiver' — like the doorposts in ch 6 or King Ahaz of ch 7} at his presence,
```
