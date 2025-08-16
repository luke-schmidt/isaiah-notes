# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands

- **Compile main template**: `./build.sh` - Compiles main.tex and opens the resulting PDF automatically on macOS
- **Manual main template compilation**: `pdflatex -output-directory=output main.tex` - Direct LaTeX compilation
- **Compile chapter files**: `cd chapters && xelatex filename.tex` - Chapter files require XeLaTeX due to Hebrew fontspec usage
- **Output locations**: 
  - Main template: `output/main.pdf`
  - Chapter files: `chapters/filename.pdf`

## Project Architecture

This is a LaTeX project for creating Isaiah Bible study guides with specialized formatting for chiastic analysis and Hebrew text. The repository contains:

### Main Document Structure
- `main.tex` - Primary document containing Bible study template and example content
- `styles/isaiah.sty` - Comprehensive style package with chiastic analysis tools, verse environments, and Hebrew text support
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

3. **`\begin{overview}`**
   - Chapter summary environment with gradient styling
   - Used with `\isaiahOverview{section_number}` for reusable content

4. **`\begin{comparisontable}`**
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
- **Hebrew Text**: `\hebrew{text}` - Proper formatting for Hebrew characters

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

**Chapter Overview**:
```latex
\begin{overview}
    \isaiahOverview{1} % Displays predefined overview content for section 1
\end{overview}
```

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
# Full build with automatic preview
./build.sh

# Manual compilation with preview generation
pdflatex -output-directory=output main.tex && magick convert -density 150 output/main.pdf[0] output/preview.png

# Alternative with poppler
pdflatex -output-directory=output main.tex && pdftoppm -png -singlefile -r 150 output/main.pdf output/preview
```

**Critical**: Always use `Read` tool on `output/preview.png` after making any template changes to verify the visual output matches expectations. The preview image provides immediate visual feedback that compilation logs cannot capture.

## TikZ Component Development Lessons

### Grid Layout Height Control Issues
When developing grid-based TikZ components, be aware of these critical challenges:

1. **`minimum height` vs actual height**: TikZ `minimum height` is often overridden by content that exceeds the minimum. Content with varying amounts (different numbers of bullet points, text length) will create inconsistent visual heights even with identical `minimum height` settings.

2. **Visual verification is essential**: LaTeX compilation success does not guarantee correct visual output. Components may compile without errors but display incorrectly. Always generate and examine preview images using `Read` tool.

3. **Content standardization**: For uniform visual appearance across grid items:
   - Standardize bullet point counts (e.g., all tall sections get 4 items, all short sections get 2 items)
   - Use consistent `\vspace{}` commands to force height differences
   - Consider using different content amounts rather than relying solely on TikZ height parameters

4. **Force height differences**: When `minimum height` alone fails:
   - Combine explicit height settings with content variations
   - Use extra `\vspace{1cm}` in taller sections
   - Reduce content in shorter sections
   - Test with aggressive height differences (e.g., 6.5cm vs 4cm) to ensure visibility

### Grid Component Structure
Example successful pattern for varying heights:
```latex
% TALL sections (1,3,4,6): 6.5cm + 4 bullet points + \vspace{1cm}
% SHORT sections (2,5): 4cm + 2 bullet points + \vspace{6pt}
\node[minimum height=6.5cm, ...] {
    \textbf{\large Section Title}
    \vspace{8pt}
    \begin{itemize}
        \item Content 1
        \item Content 2
        \item Content 3
        \item Content 4
    \end{itemize}
    \vspace{1cm}  % Force extra height
};
```

### Component Testing Workflow
1. Create isolated test files with `\usepackage{styles/components/componentname}`
2. Test with no highlighting (`\componentCommand{0}`) to see baseline layout
3. Test highlighting on both tall and short sections
4. Generate multiple preview images at each stage
5. Never assume height settings work without visual verification