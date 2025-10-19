# Notability Note-Taking Guide for Isaiah Study

This guide helps you take structured notes in Notability that can be easily converted to LaTeX chapter files using the `notes-to-tex` skill.

## Recommended Notation System

### 1. Structural Markers (Handwritten)

**For Chiastic Structures:**
```
A — Verses X-Y: Theme name
  B — Verses Z: Sub-theme
    C — Verse W: Central point
  B' — Verses V: Response theme
A' — Verses U: Conclusion theme
```

**For Simple Outlines:**
```
→ Verses X-Y: Main section
  → Verses Z: Subsection
```

**Key Principles:**
- Use consistent indentation for hierarchy
- Always include verse ranges
- Keep theme names short and clear
- Use primes (') for chiastic correspondences

### 2. Text Highlighting (Digital Highlighter)

| Color  | LaTeX Command |
|-------|------------|
| Yellow | `\highlightyellow{}` |
| Purple | `\highlightpurple{}` |
| Red |  `\highlightred{}` |
| Blue | `\highlightblue{}` |
| Orange | `\highlightorange{}` |
| Green | `\highlightgreen{}` |
| Brown | `\highlightbrown{}` |
| Gray | `\highlightgray{}` |

**Best Practices:**
- Be consistent with color meanings within a chapter
- Highlight complete phrases when possible
- Note the color mapping at the top of your page if deviating from defaults

### 3. Footnotes (Marginal Notes)

Use a clear marker system:
- **Asterisk (*)** = Translation note
- **Number in circle ①** = Cross-reference
- **Caret (^)** = Hebrew/Greek word explanation
- **Hash (#)** = Scholarly citation
- **Question mark (?)** = Question/placeholder for research

**Format:**
```
Word with asterisk* → Margin note: "Alternative translation" or "Cf. Reference"
```

### 4. Images and Visual References

**Label clearly:**
```
[Image or photo]
↓
Caption: Lebanon Cedar
```

**For side-by-side comparisons:**
```
[Image 1]        [Image 2]
Mud Bricks       Ashlar Stones
```

### 5. Cross-References

**Format:**
```
cf. Book Chapter:Verse
See also Book Chapter:Verse
Compare with Book Chapter:Verse
```

**Examples:**
- cf. Amos 1:6
- See Ex. 6:6, Deut 4:34
- Compare with Genesis 6:5, 11

### 6. Placeholder Topics

For ideas you want to expand later:

```
[Box or bracket around area]
TOPIC: "Hand Still Stretched Out"
Note: Read Ex 6:6 and Deut 4:34 - can be power to save or judge
TODO: Expand on this theme
```

### 7. Repeated Refrains

**Mark clearly:**
```
═══════════════════════
REFRAIN (appears v.12, 17, 21):
"For all this his anger has not turned away,
and his hand is stretched out still"
═══════════════════════
```

### 8. Hebrew/Greek Words

**Format for word analysis:**
```
┌─────────────────────┐
│ Justice (English)   │
│ מִשְׁפָּט (Hebrew)    │
│ mish·pat (Phonetic) │
│ God's right order   │
│ in the world (Def)  │
└─────────────────────┘
```

Or simpler:
```
Justice = מִשְׁפָּט (mish·pat)
Definition: God's right order
```

## Example Page Layout

```
╔═══════════════════════════════════════════════╗
║ Isaiah 9:8-21                                 ║
╠═══════════════════════════════════════════════╣
║                                               ║
║ STRUCTURE:                                    ║
║ A — 8-12: Nations against Israel             ║
║   B — 13-17: Leaders against Poor             ║
║ A' — 18-21: Israel against Itself            ║
║                                               ║
║ [Biblical text with highlights]               ║
║ For all this his anger has not               ║
║ turned away... ← REFRAIN (orange highlight)   ║
║                                               ║
║ NOTES:                                        ║
║ * v.8 "word" - Septuagint: "plague/death"    ║
║ ① v.12 cf. Amos 1:6 - Philistines involved   ║
║                                               ║
║ PLACEHOLDER:                                  ║
║ "Hand Stretched Out" - Ex 6:6, Deut 4:34     ║
║ Can be power to save OR judge                 ║
║                                               ║
║ IMAGES:                                       ║
║ [Photo: Mud Bricks]  [Photo: Ashlar Stones]  ║
║                                               ║
╚═══════════════════════════════════════════════╝
```

## Quick Reference Checklist

Before photographing your notes for conversion, ensure you have:

- [ ] Verse ranges clearly marked for each section
- [ ] Structural outline (chiastic or simple)
- [ ] Highlights with consistent color usage
- [ ] Footnote markers with corresponding margin notes
- [ ] Cross-references in standard format (cf. Book Ch:V)
- [ ] Image labels/captions
- [ ] Placeholder topics clearly boxed or marked
- [ ] Repeated refrains identified
- [ ] Any Hebrew/Greek words noted with transliterations

## Tips for Clean Conversion

1. **Write legibly** - The AI will OCR handwritten text
2. **Use clear sections** - Visual separation helps parsing
3. **Be explicit** - "This is a footnote" is clearer than assuming
4. **Mark relationships** - Use arrows, brackets, or lines to show connections
5. **Note deviations** - If using colors differently than standard, add a legend
6. **Keep verses together** - Don't split a verse across pages if possible
7. **Date your notes** - Helps track which notation style you were using

## Advanced Patterns

### Comparison Tables

```
┌──────────────┬──────────────┐
│ ESV          │ NIV          │
├──────────────┼──────────────┤
│ Translation  │ Translation  │
└──────────────┴──────────────┘
```

### Thematic Connections

```
Theme: EATING/DEVOURING
→ v.12: "devour Israel with open mouth"
→ v.16: "swallowed up"
→ v.20: "devour... devour... devours"
→ v.21: "devours Ephraim"
```

### Literary Devices

```
IRONY: What they do to vulnerable is what
enemies do to them (vv. 12, 16, 20-21)
```

---

## Using the Conversion Skill

Once your notes follow this structure:

1. Take a clear photo/screenshot of your notes
2. Run the skill: (skill invocation method TBD)
3. Review the AI's interpretation
4. Confirm or correct the detected elements
5. Approve the generated LaTeX file
6. Manually fill in placeholder sections as you study further

Remember: The more consistent your notation, the smoother the conversion process!
