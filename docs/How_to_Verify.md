# 📋 How to Verify KST Statistical Claims

## Overview

This guide explains how to independently verify the statistical claims made by the Kelly Standard Transcription (KST) methodology for Voynich Manuscript analysis.

---

## 🎯 Claims to Verify

| # | Claim | Value | Verification Method |
|:--|:------|:------|:--------------------|
| 1 | Total manuscript lines | 5,390 | Count lines in KST Cleaner output |
| 2 | Dictionary coverage | 99.9% | Run coverage_calculator.py |
| 3 | Dictionary entries | 799 | Count entries in dictionary_keys |
| 4 | CEVA-English probability | 4.8×10⁻¹² | Run probability_calculator.py |
| 5 | Most frequent word | "daiin" (861+) | Cross-check with voynichese.com |

---

## 📥 Step 1: Obtain Source Data

### Option A: Use Public CEVA Data

1. Visit [voynichtranscription.co.uk](https://voynichtranscription.co.uk)
2. Download transcription data in CEVA format
3. Process through KST Cleaner v1.11

### Option B: Use Pre-Cleaned Sample Data

Contact us for sample KST-cleaned datasets for verification purposes.

---

## 🔧 Step 2: Verify Line Count (Claim #1)

### Using KST Cleaner

1. Open `tools/kst_cleaner_v1_11.html` in a web browser
2. Paste raw CEVA data
3. Click "PROCESS"
4. Check the statistics panel for total line count

### Expected Result

```
Total Lines: 5,390
Pages: 225
```

### Verification Notes

- Lines may vary slightly depending on CEVA version used
- KST Cleaner v1.10+ includes `[?UVA]` markers for unreadable characters
- Ensure all manuscript sections are included

---

## 📊 Step 3: Verify Coverage Rate (Claim #2)

### Run Coverage Calculator

```bash
cd tools/
python coverage_calculator.py --input your_kst_data.tsv
```

### Expected Output

```
📊 RESULTS
=====================================
Total words processed:     37,638
Words in dictionary:       37,600
Words not in dictionary:   38
✨ COVERAGE RATE:          99.9%
```

### Understanding the Calculation

Coverage = (Words with dictionary definition) / (Total words) × 100%

The calculator uses the "onion peeling" method:
- First tries direct dictionary lookup
- Then tries recursive decomposition (e.g., "cheody" = "che" + "o" + "dy")

### Cross-Verification

1. Check undefined words list
2. Verify these are genuinely rare or corrupted text
3. Compare against voynichese.com word list

---

## 🎲 Step 4: Verify Probability Calculation (Claim #4)

### Run Probability Calculator

```bash
python probability_calculator.py --matches 8 --alphabet 26
```

### Expected Output

```
🎯 P(all 8 match by chance) = 4.80E-12
                            = 4.80 × 10⁻¹²

Odds against chance:  1 in 208,827,064,576
```

### The Calculation

```
P = (1/26)^8
P = (0.0385)^8
P = 4.80 × 10⁻¹²
```

### What This Means

If CEVA letters randomly corresponded to English letters:
- Each letter has 1/26 chance of matching
- 8 independent matches: (1/26)^8
- The probability is astronomically small
- This suggests the correspondence is NOT random

### Assumptions to Note

1. Uniform distribution assumption
2. Independence assumption
3. 26-letter English alphabet
4. 8 clear correspondences identified

---

## 📈 Step 5: Verify Word Frequencies (Claim #5)

### Cross-Reference with Voynichese.com

1. Visit [voynichese.com](https://voynichese.com)
2. Navigate to word frequency statistics
3. Compare top words with our `word_frequency_sample.csv`

### Expected Matches

| Rank | KST Claim | Voynichese.com |
|:-----|:----------|:---------------|
| 1 | daiin (861+) | daiin (~850-870) |
| 2 | aiin (527+) | aiin (~520-530) |
| 3 | chedy (412+) | chedy (~400-420) |

### Notes on Frequency Variations

- Exact counts may vary based on transcription version
- Word boundaries may differ between systems
- Focus on relative rankings, not exact numbers

---

## ✅ Verification Checklist

Use this checklist to document your verification:

```markdown
## My Verification Report

**Date**: ____________________
**Name**: ____________________
**Affiliation**: ____________________

### Data Source
- [ ] Used voynichtranscription.co.uk
- [ ] CEVA version used: ________
- [ ] Trans versions: H / A / Y

### Claim 1: Line Count
- [ ] Verified
- My count: ________
- KST claim: 5,390
- Difference: ________
- Notes: ____________________

### Claim 2: Coverage Rate
- [ ] Verified
- My calculation: ________%
- KST claim: 99.9%
- Difference: ________
- Notes: ____________________

### Claim 3: Dictionary Entries
- [ ] Verified
- My count: ________
- KST claim: 799
- Notes: ____________________

### Claim 4: Probability
- [ ] Verified
- My calculation: ________
- KST claim: 4.8×10⁻¹²
- Notes: ____________________

### Claim 5: Word Frequencies
- [ ] Verified against voynichese.com
- Top word matches: ________
- Notes: ____________________

### Overall Assessment
- [ ] All claims verified
- [ ] Some discrepancies found (details below)
- [ ] Major issues found (details below)

### Additional Notes
____________________
____________________
____________________
```

---

## 🤝 Submit Your Verification

After completing verification, please submit your findings:

1. **GitHub Issue**: Open an issue with your verification report
2. **Label**: Use `verification-result` label
3. **Include**: Your completed checklist and any supporting data

Successful verifiers will be acknowledged in [ACKNOWLEDGMENTS.md](../ACKNOWLEDGMENTS.md)

---

## ❓ FAQ

### Q: Why can't I get exactly 5,390 lines?

Different CEVA versions may have slightly different line counts. Also:
- Some pages have merged/split lines in different versions
- Unreadable characters handled differently
- Make sure to use Trans H priority as primary source

### Q: My coverage is 98% instead of 99.9%?

Check:
- Are you using the full V15 dictionary structure?
- Is the onion peeling algorithm working correctly?
- Are there encoding issues with your input file?

### Q: The probability calculation seems too simple?

The calculation makes simplifying assumptions. The real statistical significance may differ based on:
- Actual English letter frequency distribution
- Linguistic constraints
- Historical context of potential encoding

---

## 📞 Need Help?

If you encounter issues during verification:

1. Check existing GitHub Issues
2. Open a new Issue with details
3. Include: your environment, input data source, and error messages

---

**oror.sheey!** 🔥⚡💜
