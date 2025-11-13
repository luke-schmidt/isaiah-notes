---
description: Highlight words in Isaiah chapters interactively
---

You are helping to highlight words in an Isaiah chapter tex file. The user will give you words or word pairings one at a time, and you will highlight them using available highlighter colors from the styles file.

## Process:
1. For each word/phrase the user provides, choose a highlighter color that hasn't been used yet in the current chapter
2. Apply the highlight by wrapping the word/phrase with the appropriate `\highlight{colorname}{text}` command
3. Track which colors have been used to ensure variety
4. Create a new highlighter color if needed (all existing are taken) and update this claude command if that ends up happening

## Available highlighter colors (from /Users/luke.schmidt/code/isaiah/styles/components/formatting.sty):
- `\highlightred` (red)
- `\highlightpurple` (purple)
- `\highlightgray` (gray)
- `\highlightbrown` (brown)
- `\highlightgreen` (green)
- `\highlightblue` (blue)
- `\highlightlightblue` (light blue)
- `\highlightdarkblue` (dark blue)
- `\highlightsilver` (silver/light gray)
- `\highlightorange` (orange)
- `\highlightyellow` (yellow)
- `\highlightaqua` (aqua/cyan)
- `\highlightdarkred` (dark red)
- `\highlightpink` (pink)
- `\highlightteal` (teal)
- `\highlightlightgray` (light gray)
- `\highlightlime` (lime green)
- `\highlightcoral` (coral)
- `\highlightcyan` (cyan)
- `\highlightolive` (olive green)

## Instructions:
1. First, read the current chapter file to see what's already highlighted
2. Wait for the user to provide words/phrases one at a time
3. For each word/phrase:
   - Choose a color that hasn't been used yet
   - Apply the highlight to ALL occurrences of that word/phrase in the chapter
   - Confirm which color you used

## Notes:
- Pick colors strategically based on what hasn't been used yet
- Be ready to highlight multiple occurrences of the same word throughout the chapter
- The user will provide words one-by-one, so wait for their input between highlights
