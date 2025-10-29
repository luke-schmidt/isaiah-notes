# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

- **Compile main template**: `./build.sh` - Compiles main.tex and opens the resulting PDF automatically on macOS
- **Manual main template compilation**: `pdflatex -output-directory=output main.tex` - Direct LaTeX compilation
- **Compile chapter files**: Chapter files require XeLaTeX due to Hebrew fontspec usage
  - Navigate into the specific chapter directory: `cd chapters/isaiah-10-1-4`
  - Compile with XeLaTeX: `xelatex isaiah-10-1-4.tex`
  - PDF will be created in the same directory
- **Output locations**:
  - Main template: `output/main.pdf`
  - Chapter files: `chapters/chapter-name/chapter-name.pdf` (in the same directory as the .tex file)

## Project Architecture

This is a LaTeX project for creating Isaiah Bible study guides with specialized formatting for chiastic analysis and Hebrew text. The repository contains:

### Main Document Structure
- `main.tex` - Primary document containing Bible study template and example content
- `styles/` - Comprehensive styles and components package with chiastic analysis tools, verse environments, and Hebrew text support
- `chapters/` - Individual Isaiah study files (isaiah-2-6-22.tex, isaiah_1_2-31.tex, isaiah_2_1-5.tex) with their compiled outputs

### Isaiah Study Template System
The template system provides specialized environments for biblical analysis:

**Core Environments**:

1. **`\begin{biblicaloutline}[optional title]`**
   - Creates bordered sections with optional headers that appear above the border
   - Use TikZ-based styling with rounded corners and custom colors

2. **`\begin{chiasticoutline}[optional title]`**
   - Advanced environment for chiastic structure analysis
   - Automatic indentation levels for nested chiastic patterns
   - Supports complex verse arrangements with `\chiasticverse[marker]{indent}{text}`

3. **`\begin{comparisontable}`**
   - Side-by-side comparison environment for parallel passages
   - Structured layout for textual analysis

**Text Layout Commands**:
- `\subsectionheader{Title}` - Bold headers with horizontal lines
- `\begin{versesection}[marker]` - Two-column layout with optional left-aligned markers
- `\begin{indentedsubsection}` - Custom indentation environment
- `\poetryline{text}` - Specialized poetry formatting
- `\versenum{number}` - Superscript verse numbers

**Text Highlighting** (complete set):
- **Colors**: `\highlightred{text}`, `\highlightpurple{text}`, `\highlightbrown{text}`, `\highlightgreen{text}`, `\highlightblue{text}`, `\highlightsilver{text}`, `\highlightorange{text}`, `\highlightyellow{text}`, `\highlightaqua{text}`, `\highlightgray{text}`
- **Bold Colors**: `\boldred{text}`, `\boldblue{text}`
- **Hebrew Text**: `\hebrew{text}` - Basic Hebrew text formatting
- **Hebrew Word Analysis**: `\hebrewword{English}{Hebrew}{Pronunciation}{Definition}` - Card-style analysis with colored boxes for each component (leave definition empty `{}` for no definition box)

**Scholarly Quotes** (with proper attribution):
```latex
\begin{quote}
\textit{"Quote text in italics with proper quotation marks"}\\\\
\hfill --- Author Name, \textit{Book Title}
\end{quote}
```
- Use `\\\\` for paragraph breaks within quotes
- Book titles always italicized with `\textit{}`
- Right-aligned attribution with `\hfill ---`
- URLs can be added after book titles for web sources
  - Hebrew text in yellow box (using proper Hebrew fontspec)
  - Pronunciation/transliteration in blue box  
  - Optional definition section in green box (omit if definition parameter is empty)
  - Card-style layout with rounded borders and visual separation

### MacTeX Path Configuration
The build.sh script automatically detects and configures MacTeX paths for multiple installation years (2024, 2025) and fallback locations.

### Template Usage Patterns

**Basic Biblical Outline**:
```latex
\begin{biblicaloutline}[Section Title]
    \subsectionheader{First Section}
    \begin{versesection}[A]
        \versenum{1} Biblical text with \highlightpurple{highlighting}...
    \end{versesection}
\end{biblicaloutline}
```

**Chiastic Structure Analysis**:
```latex
\begin{chiasticoutline}[Chiastic Structure - Isaiah 2:6-22]
    \subsectionheader{A. Divine Judgment Theme}
    \chiasticverse[A]{0}{\versenum{6} For you have rejected your people, the house of Jacob...}
    
    \subsectionheader{B. Human Pride}
    \chiasticverse[B]{1}{\versenum{7-8} Their land is filled with silver and gold...}
    
    \subsectionheader{C. Central Message}
    \chiasticverse[C]{2}{\versenum{11} The \highlightred{lofty looks of man} shall be humbled...}
    
    \subsectionheader{B'. Divine Response}
    \chiasticverse[B']{1}{\versenum{12-16} For the Lord of hosts has a day...}
    
    \subsectionheader{A'. Final Judgment}
    \chiasticverse[A']{0}{\versenum{17-22} The loftiness of man shall be bowed down...}
\end{chiasticoutline}
```

**Chiastic Structure with Sublabels**:
```latex
\begin{chiasticoutline}[Advanced Chiastic Analysis]
    \chiasticverselabel[A]{0}{\versenum{1} Opening text...}{Opening}
    \chiasticverselabel[B]{1}{\versenum{2-3} Middle content...}{Theme}
    \chiasticverselabel[B']{1}{\versenum{4-5} Corresponding content...}{Response}
    \chiasticverselabel[A']{0}{\versenum{6} Closing text...}{Conclusion}
\end{chiasticoutline}
```

**Hebrew Word Analysis**:
```latex
% Basic Hebrew word with definition
\hebrewword{Justice}{מִשְׁפָּט}{mish.pat}{God's right order in the world.}

% Hebrew word with empty definition (no definition box shown)
\hebrewword{Bloodshed}{מִשְׂפָּח}{mis.pach}{}

% Advanced example with detailed definition
\hebrewword{Virgin}{עַלְמָה}{al.mah}{young woman of marriable age}
```

**Chapter Overview**:

The current chapters demonstrate these patterns with detailed Isaiah analysis including chiastic structures, Hebrew text integration, and thematic highlighting.

## Visual Testing Workflow for Claude

**Required tools installed**: ImageMagick and Poppler are now available for automatic preview generation.

When making changes to LaTeX templates or formatting:

1. **Always test changes visually** - LaTeX compilation success doesn't guarantee correct visual output
2. **Use the build script**: `./build.sh` automatically generates both PDF and PNG preview at 150 DPI
3. **Read the preview image**: Use `Read` tool on `output/preview.png` to verify visual changes
4. **Check for layout issues**: Look for text overflow, incorrect spacing, broken borders, or misaligned elements
5. **Validate before completing**: Never mark template changes as complete without visual verification

### Automatic Preview Generation
The build script now automatically generates `output/preview.png` using:
- **Primary method**: ImageMagick (`convert` command)
- **Fallback method**: Poppler (`pdftoppm` command)
- **Resolution**: 150 DPI for optimal balance of quality and file size

### Common Visual Issues to Check
- Header positioning relative to border (should overlay/interrupt the top border)
- Border interruption effects that cause layout breaks
- Text overflowing boxes (overfull hbox warnings in log)
- Incorrect indentation or alignment
- Missing or broken highlighting
- Subsection headers not displaying properly
- Font size and prominence of section headers

### Testing Commands
```bash
# Full build with automatic preview (for main template)
./build.sh

# Manual compilation with preview generation (for main template)
pdflatex -output-directory=output main.tex && magick convert -density 150 output/main.pdf[0] output/preview.png

# Alternative with poppler (for main template)
pdflatex -output-directory=output main.tex && pdftoppm -png -singlefile -r 150 output/main.pdf output/preview

# Chapter file compilation with preview (example for Isaiah 10:1-4)
cd chapters/isaiah-10-1-4 && xelatex isaiah-10-1-4.tex && magick "isaiah-10-1-4.pdf[0]" preview.png

# Workflow for compiling and previewing chapter files:
# 1. Navigate to chapter directory (or use full path in commands)
# 2. Compile with xelatex (creates PDF in same directory)
# 3. Generate preview PNG with magick (use quotes around PDF path with [0])
# 4. Use Read tool to view the preview.png
```

**Critical**: Always use `Read` tool on the output .png file after making any template changes to verify the visual output matches expectations. The preview image provides immediate visual feedback that compilation logs cannot capture.
