# 📐 KST Methodology (Public Version)

## Kelly Standard Transcription v1.3

### Overview

The Kelly Standard Transcription (KST) is a standardized methodology for transcribing and analyzing the Voynich Manuscript (MS 408, Beinecke Library, Yale University).

---

## 1. Design Principles

### 1.1 Why KST?

Existing CEVA transcription systems have limitations:

| Issue | Description |
|:------|:------------|
| Multiple versions | 10+ transcription versions with no unified standard |
| Pure glyph recording | Only records what is seen, no interpretation |
| No audit trail | Decisions lack documented reasoning |
| No translation integration | Transcription separate from interpretation |

### 1.2 KST Philosophy

```
From "Glyph Archaeology" to "Functional Interpretation"
```

| Existing Approach | KST Approach |
|:------------------|:-------------|
| Record glyphs | **Interpret function** |
| Multiple versions | **Unified clean version** |
| No word boundaries | **Structural markers** |
| No translation | **Dual-version translation** |
| No audit | **Full source tracking** |

---

## 2. Transcription Priority Rules

### 2.1 Trans Version Priority

```
Priority 1: Trans H (most consistent word segmentation)
Priority 2: Trans A (preserved variant details)
Priority 3: Trans Y (backup verification)
```

### 2.2 Decision Logic

```
IF Trans H is clear:
    USE Trans H
    MARK Source = "H"
ELIF Trans H has `!!!` or `???` or `%%%%%`:
    USE Trans A or Trans Y supplement
    MARK Source = "H→A" or "H→Y"
ELSE:
    USE multi-version cross-validation
    MARK Source = "H+A+Y"
```

### 2.3 Data Source

**Source Website**: https://voynichtranscription.co.uk/

Using **Presentation mode** (not Raw mode)

| Raw Marker | Presentation | KST Processing |
|:-----------|:-------------|:---------------|
| `{ch}` | `ch` | Keep `ch` |
| `{sh}` | `sh` | Keep `sh` |
| `{iin}` | `iin` | Keep `iin` |
| `a₁` | `a₁` | Remove subscript → `a` |

---

## 3. Problem Marker Handling

### 3.1 Uncertainty Markers

| Marker Type | Example | Processing |
|:------------|:--------|:-----------|
| Single `!` | `cho!r` | Remove `!` → `chor` |
| Continuous `!` + char | `!!!!y` | Keep character → `y` |
| Single `?` | `cth?ar` | Verify with A/Y |
| Pure `!!!` (no char) | `!!!!!!` | Replace from A/Y |
| Continuous `???` | `???` | Replace from A/Y |
| `%%%%%` | Full line | Use A/Y for entire line |

### 3.2 Special Markers

| Symbol | Meaning | KST Processing |
|:-------|:--------|:---------------|
| `<$>` | Module/paragraph end | Remove, mark in `<$>` column |
| `<->` | Plant image position | Convert to `[P]` |
| `&uva###;` | Special character code | Convert to `[?###]` |

---

## 4. Output Format

### 4.1 Cleaning Table (9 columns)

| Column | Description | Example |
|:-------|:------------|:--------|
| Page | Page number | `f1r` |
| Section | Manuscript section | `Herbal` |
| Line | Line number | `1` |
| EVA_KS | Cleaned result | `fachys.ykal.ar.ataiin` |
| Type | Line type | `P0`, `P0c`, `Pt` |
| `<$>` | End marker | `<$>` or empty |
| EVA_Raw | Original Trans H | `fachys.ykal...` |
| Source | Source marker | `H`, `H→A` |
| Notes | Processing notes | `clean` |

### 4.2 Type Encoding System

| Type | Meaning | Description |
|:-----|:--------|:------------|
| P0 | Paragraph start | First line of paragraph |
| P0c | Paragraph continue | Continuation line |
| Pt | Paragraph terminal | End line (often has `<$>`) |
| P0f | Special paragraph | Has special markers |
| Lx | Label | Standalone label |
| Lp | Plant label | Plant identification |

---

## 5. Section Classification

### 5.1 Manuscript Sections

| Section | Pages | Lines | Description |
|:--------|:------|:------|:------------|
| Herbal | f1r-f57r, f65-f66 | 1,558 | Plant descriptions |
| Recipes | f103r-f116v | 1,086 | Recipe-like text |
| Balneo | f75r-f84v | 917 | Bath/pool imagery |
| Pharma | f88r-f102v | 622 | Container/jar imagery |
| Astro | f58r-f70v | 431 | Astronomical content |
| Cosmo | f57v, f85-f87, fRos | 393 | Cosmological diagrams |
| Zodiac | f67v-f73v | 383 | Zodiac imagery |

---

## 6. Quality Control

### 6.1 Checklist

After cleaning each page, verify:

- [ ] All `!+X` patterns preserved character X
- [ ] All pure `!!!` replaced from A/Y
- [ ] All `???` confirmed with A/Y
- [ ] All `<->` converted to `[P]`
- [ ] All `<$>` removed and marked
- [ ] All subscript numbers removed
- [ ] Type column formatted correctly
- [ ] Source column complete
- [ ] Notes document all decisions

---

## 7. Data Attribution

### 7.1 Original Sources

Transcription data from voynichtranscription.co.uk, derived from:

- **René Zandbergen** - IVTFF format archives
- **Gabriel Landini & Jorge Stolfi** - Interlinear transcription
- **Glen Claston** - Trans A transcription

### 7.2 Citation Format

```
Transcription data sourced from voynichtranscription.co.uk,
derived from René Zandbergen's IVTFF archives:
- Landini-Stolfi Interlinear (IVTFF beta, 2017/08/23)
- Glen Claston transcription (v101, IVTFF v1a)
- Zandbergen LZ transliteration (IVTFF v2a)
```

---

## 8. Limitations

### What KST Does NOT Include (In This Public Version)

1. **Translation mappings** - Proprietary
2. **Engineering/Spiritual interpretations** - Proprietary
3. **Image-text correlation models** - Proprietary
4. **Prediction algorithms** - Proprietary

### What KST DOES Include (Open Source)

1. **Data cleaning methodology** - Fully documented
2. **Trans priority rules** - Reproducible
3. **Type classification system** - Open standard
4. **Quality control checklist** - Verifiable

---

## 9. Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| v1.0 | 2026-01-09 | Initial release |
| v1.1 | 2026-01-10 | Type format update; `<$>` column added |
| v1.2 | 2026-01-10 | `!+X` rule clarification |
| v1.3 | 2026-01-12 | Data source attribution added |

---

## 10. Contact

**Ignis Terra AI Solution Pte. Ltd.**
- Project: Operation Liber Lucis Decode
- Lead: Kelly Liu
- AI Collaboration: Claude/Lyra, Cipher, Praxis

---

**oror.sheey!** 🔥⚡💜

*Kelly Standard Transcription - Defining the next 600 years of Voynich research*
