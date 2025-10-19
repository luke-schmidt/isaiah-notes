---
description: Convert Notability notes to LaTeX
---

# Notes to LaTeX Converter

You are helping convert handwritten Notability notes into structured LaTeX chapter files for Isaiah Bible study guides.

## Your Task

When the user provides a screenshot of their Notability notes, you will:

1. **Analyze the image** and extract:
   - Biblical text content (use OCR for typed text, interpret handwritten annotations)
   - **Blue circles**: General notes and commentary (with optional blue title text nearby)
   - **Red circles**: Literary/chiastic structure elements
   - **Purple circles**: Images that need to be added
   - **Black stars (★)**: Footnotes (one by the word, one by the note)
   - Highlighted text (various colors for repeated words - no fixed color meanings)
   - Verse ranges and section divisions

2. **Interactive Confirmation** - Present your findings in structured format:
   - "**Blue circles (notes/commentary)**: [list sections with optional titles]"
   - "**Red circles (literary structure)**: [list structural elements and verse ranges]"
   - "**Purple circles (images)**: [list image locations with labels]"
   - "**Black stars (footnotes)**: [list word + footnote pairs]"
   - "**Highlights detected**: [list repeated words with colors]"
   - Ask user to confirm or correct each category

3. **Generate a detailed prompt** (similar to `/new-chapter-template` format) that includes:
   - Chapter/verse range
   - Overview structure with verse breakdowns
   - Highlight specifications (word/phrase + color)
   - Footnote specifications (word + explanation)
   - Placeholder topics (title + brief description)
   - Image references (filename + caption)
   - Any special formatting notes

4. **Create the .tex file** using the generated prompt

## Reference Materials

### Notation Legend
Refer to `.claude/notes-legend.json` for mapping visual annotations to LaTeX commands.

### Example Structure
The user's existing chapter files (e.g., `chapters/isaiah-9-8-21/isaiah-9-8-21.tex`) demonstrate the target output format.

### Available LaTeX Environments
From `CLAUDE.md`:
- `\begin{biblicaloutline}[title]` - Main text sections
- `\begin{chiasticoutline}[title]` - Chiastic structure analysis
- `\begin{overview}{title}` with `\overviewsection[level]{content}` - Chapter overview
- `\begin{versesection}{indent}` - Verse formatting
- `\poetryline{text}` - Individual verse lines
- `\versenum{n}` - Verse numbers
- `\sectionwordfootnote{word}{note}` - Footnotes
- Highlights: `\highlightyellow{}`, `\highlightpurple{}`, `\highlightred{}`, `\highlightblue{}`, `\highlightorange{}`, etc.
- `\hebrewword{English}{Hebrew}{Pronunciation}{Definition}` - Hebrew word analysis
- Images: standard `\includegraphics` with captions

### Document Structure Pattern
```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{../../styles/isaiah}
\usepackage{../../styles/components/threeBoxGrid}

\begin{document}

% Chiastic overview showing where this passage fits
\isaiahChiasticOverview{level}

\newpage

% Three-box grid showing context (previous, current, next sections)
\threeBoxGrid{level}{Title}{Box1 content}{Box2 content}{Box3 content}

% Overview with structural breakdown
\begin{overview}{Chapter:Verses — Overview}
\overviewsection[0]{\textbf{Verses X-Y: Theme}}
\overviewsection[1]{\textbf{Verses Z: Sub-theme}}
\end{overview}

\newpage

% Main content with biblical outlines
\begin{biblicaloutline}[Section Title]
    \begin{versesection}{2em}
        \poetryline{\versenum{X} Text with \highlightcolor{highlighting}...}
    \end{versesection}
\end{biblicaloutline}

% Commentary sections
{\large\bfseries Commentary Title}
\vspace{1em}
Explanation text...

% Images (side-by-side pattern)
\begin{center}
\begin{minipage}[t]{0.45\textwidth}
\centering
\includegraphics[width=\textwidth]{image1.png}\\
\vspace{0.5em}
Caption 1
\end{minipage}
\hspace{0.05\textwidth}
\begin{minipage}[t]{0.45\textwidth}
\centering
\includegraphics[width=\textwidth]{image2.png}\\
\vspace{0.5em}
Caption 2
\end{minipage}
\end{center}

\end{document}
```

## Analysis Guidelines

### Circle Detection (PRIMARY MARKERS)

**Blue Circles** - Notes/Commentary:
- Identify content circled in blue ink
- Look for optional blue title text written near the circle
- Convert to `\begin{biblicaloutline}[title]` or commentary sections
- Blue title becomes section header

**Red Circles** - Literary Structure:
- Identify content circled in red ink
- These mark chiastic or structural elements (A, B, C, A', B', etc.)
- Convert to `\begin{chiasticoutline}` with `\chiasticverse` commands
- Indentation levels indicate chiastic depth

**Purple Circles** - Images:
- Identify areas circled in purple
- Look for nearby labels/captions
- Create `\includegraphics` placeholders with appropriate captions

**Black Stars (★)** - Footnotes:
- Look for small black star symbols
- One star appears by the word, one by the corresponding note
- Convert to `\sectionwordfootnote{word}{explanation}`

### Interpreting Highlights
- Highlights are **random colors** used to mark repeated words or thematic connections
- **Do NOT assume fixed meanings** for specific colors
- Same color = likely thematically related words
- Ask user to confirm which words share highlights and what color to use

### Placeholder Topics
When notes say things like "expand on this" or have incomplete thoughts, create placeholder sections:
- Extract the topic/question as the header
- Summarize any visible notes as the initial content
- User will fill in details later

## Interaction Flow

1. **Initial Analysis**
   ```
   I've analyzed your notes for Isaiah X:Y-Z. Here's what I found:

   **Blue circles (notes/commentary):**
   - Circle 1: [content] with title "[blue title text]"
   - Circle 2: [content] (no title)

   **Red circles (literary structure):**
   - Verses X-Y: [structural element A]
   - Verses Z: [structural element B]

   **Purple circles (images):**
   - Image 1: [label/caption]
   - Image 2: [label/caption]

   **Black stars (footnotes):**
   - Verse X: "word" ★ → [footnote content]
   - Verse Y: "phrase" ★ → [footnote content]

   **Highlights detected:**
   - "phrase" in yellow (verses X, Y)
   - "word" in purple (verse Z)

   Does this look correct? Any corrections or additions?
   ```

2. **Refinement**
   User provides corrections, you adjust the interpretation.

3. **Generate Prompt**
   Create a detailed prompt similar to the `/new-chapter-template` format.

4. **Create File**
   Ask for confirmation, then generate the `.tex` file in the appropriate chapter directory.

## Important Notes

- Always ask before creating files - show the generated prompt first
- Image filenames should match the labels in the notes (lowercased, hyphenated)
- Maintain consistency with existing chapter file patterns
- When uncertain about interpretation, ask rather than guess
- Hebrew text requires special handling with fontspec/XeLaTeX
- Preserve the user's voice in commentary sections where notes are present

## Starting the Workflow

When invoked, greet the user and ask them to share their Notability screenshot. Then begin the analysis and interactive confirmation process.
