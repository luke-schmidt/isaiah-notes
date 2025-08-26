# Right-Aligned Note Options for Isaiah Study Template

Based on your request for subtle right-aligned notes next to biblical verses, I've implemented three different approaches:

## Option 1: Margin Notes
**Command**: `\rightnote{your note text}`

**Usage**: Add `\rightnote{text}` anywhere in your verse content
```latex
\versenum{6} For you have rejected your people,\rightnote{Historical context}
```

**Visual Description**: 
- Notes appear in the right margin
- Small gray text that doesn't interfere with main content
- Automatically positioned alongside the verse line
- Most subtle option - stays completely out of the main text flow

## Option 2: Side-by-Side Layout  
**Commands**: `\versewithsidenote` environment + `\setrightnote{text}`

**Usage**:
```latex
\setrightnote{This verse shows God's rejection due to foreign influences}
\begin{versewithsidenote}[A]
\versenum{6} For you have rejected your people,
\poetryline the house of Jacob,
\end{versewithsidenote}
```

**Visual Description**:
- Main verse content takes ~65% of width
- Right note takes ~27% of width in a dedicated column
- Note appears alongside the entire verse section
- Good for longer explanatory notes
- More prominent than margin notes but still subtle

## Option 3: Enhanced Chiastic Structure with Notes
**Command**: `\chiasticversewnote[marker]{level}{content}{note}`

**Usage**:
```latex
\chiasticversewnote[A]{0}{
\versenum{6} For you have rejected your people,
\poetryline the house of Jacob,
}{Foreign influence corrupting God's people}
```

**Visual Description**:
- Integrates directly with your existing chiastic structure environments
- Note appears in a right column alongside each chiastic element
- Maintains all chiastic indentation and formatting
- Perfect for structural analysis notes

## Implementation Details

All three options:
- Use gray text (70% opacity) to keep notes subtle
- Are fully responsive to your existing environments
- Maintain proper spacing and alignment with verse content
- Support multi-line notes when needed

## Recommendation

For different use cases:
- **Option 1 (Margin Notes)**: Best for brief contextual notes, word definitions, or cross-references
- **Option 2 (Side-by-Side)**: Best for longer explanations or thematic notes
- **Option 3 (Chiastic Notes)**: Best when analyzing structure and want notes tied to specific chiastic elements

The implementations are ready to test. Would you like me to create a working example with actual LaTeX compilation once you have a chance to review these options?