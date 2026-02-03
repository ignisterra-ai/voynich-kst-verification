# 🔮 KST Verification Tools
## Kelly Standard Transcription - Open Verification Framework

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Methodology](https://img.shields.io/badge/KST-v1.3-purple.svg)](docs/KST_Methodology_Public.md)
[![Dictionary](https://img.shields.io/badge/Dictionary-V15.0-gold.svg)](data/dictionary_v15_keys.json)

**🌐 Language**: [English](README.md) | [繁體中文](README_zh-TW.md)

---

## 🎯 Purpose

This repository provides **open verification tools** for the Kelly Standard Transcription (KST) methodology applied to the Voynich Manuscript (MS 408).

**Our goal**: Enable independent researchers to verify our statistical claims without revealing proprietary translation mappings.

> *"We don't claim to have 'solved' the Voynich Manuscript. We claim to have discovered statistically significant patterns that deserve verification."*

**In this repo, we only ask one thing:**

> Given public CEVA data and our open tools, **do our published statistics check out?**

This is not a place to argue about "whether the decoding is correct" — it's a place to verify the numbers.

---

## 📊 Statistical Claims for Verification

| Claim | Expected | How to Verify |
|:------|:---------|:--------------|
| Total manuscript lines processed | **5,390** | Run `coverage_calculator.py` |
| Dictionary coverage rate | **99.9% (5387/5390 lines)** | `coverage_calculator.py` + `dictionary_v15_keys.json` |
| Dictionary entries | **799 keys** | Count entries in dictionary |
| CEVA-English mapping probability | **≈ 4.8 × 10⁻¹²** | Run `probability_calculator.py` |
| Most frequent word "daiin" | **≥ 861 tokens** | Cross-check with voynichese.com |

**Verification Protocol**: Run the tool, compare your result to the "Expected" column. If they match, the claim is verified.

---

## ⚠️ Known Missing Folios

The Voynich Manuscript has **14 missing folios (28 pages)** that are not included in any transcription database:

| Section | Missing Folios | Quire | Notes |
|:--------|:---------------|:------|:------|
| Herbal | f12 | Quire II | Stub visible at binding |
| Astro | f59, f60, f61, f62, f63, f64 | Quire VIII | Central bifolia group removed |
| Zodiac | f74 | Quire XII | Conjugate stub visible |
| Pharma | f91, f92, f97, f98 | Quire XVI | Two bifolia removed |
| Recipes | f109, f110 | Quire XVIII | Central bifolium removed |

**Total**: 14 folios = 28 pages not in transcription data

This is consistent with the original manuscript condition at Yale Beinecke Library. Our **5,390-line count reflects all extant text** — there is no "missing data" in our database; these pages simply do not exist in the physical manuscript.

---

## 🛠️ Tools Provided

| Tool | Description | File |
|:-----|:------------|:-----|
| **KST Cleaner v1.11** | CEVA → EVA_KS standardization | `tools/kst_cleaner_v1_11.html` |
| **Coverage Calculator** | Verify translation coverage claims | `tools/coverage_calculator.py` |
| **Probability Calculator** | CEVA-English correspondence probability | `tools/probability_calculator.py` |
| **Independent Verification** | Complete verification script | `verification/independent_verification.py` |

### 🔐 Scope

This repository provides **statistical verification tools only**. The complete translation system remains proprietary and patent-pending.

---

## 📁 Repository Structure

```
voynich-kst-verification/
│
├── README.md                           # English documentation
├── README_zh-TW.md                     # 繁體中文說明
├── LICENSE                             # Apache 2.0
├── CITATION.cff                        # Academic citation format
├── CONTRIBUTING.md                     # How to contribute
├── ACKNOWLEDGMENTS.md                  # Verification contributors
│
├── tools/
│   ├── kst_cleaner_v1_11.html          # Data cleaning tool
│   ├── coverage_calculator.py          # Coverage verification
│   └── probability_calculator.py       # Probability calculation
│
├── data/
│   ├── dictionary_v15_keys.json        # Dictionary keys only (no translations)
│   ├── section_statistics.csv          # Per-section line counts
│   └── word_frequency_sample.csv       # Top 50 word frequencies
│
├── verification/
│   └── independent_verification.py     # Complete verification script
│
└── docs/
    ├── KST_Methodology_Public.md       # Public methodology description
    ├── Statistical_Claims.md           # Detailed statistical claims
    └── How_to_Verify.md                # Step-by-step verification guide
```

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/ignisterra-ai/voynich-kst-verification.git
cd voynich-kst-verification
```

### 2. Verify Coverage Claims

```bash
python tools/coverage_calculator.py --input your_kst_data.tsv
```

### 3. Verify Probability Claims

```bash
python tools/probability_calculator.py
```

### 4. Cross-Reference with External Sources

Visit [voynichese.com](https://voynichese.com) to independently verify word frequencies.

---

## 📐 Methodology Overview

### The KST Pipeline

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  CEVA Raw Data      │ ──▶ │   KST Cleaner       │ ──▶ │  Standardized       │
│  (Multi-version)    │     │    (v1.11)          │     │   EVA_KS            │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
                                                                │
                                                                ▼
                              ┌──────────────────────────────────────────────────┐
                              │         Coverage Verification                    │
                              │  (This repository - fully open)                  │
                              └──────────────────────────────────────────────────┘
                                                                │
                                                                ▼
                              ┌──────────────────────────────────────────────────┐
                              │         Translation Engine                       │
                              │  (Protected - not in this repo)                  │
                              └──────────────────────────────────────────────────┘
```

### Trans Version Priority

```
Priority 1: Trans H (most consistent word segmentation)
Priority 2: Trans A (variant details preserved)
Priority 3: Trans Y (backup verification)
```

---

## 🤝 Invitation to Verify

We welcome independent verification of our statistical claims!

### What You Can Do

1. **Verify Statistics**: Run our tools against public CEVA data
2. **Find Errors**: Report any calculation mistakes
3. **Challenge Claims**: Provide counter-evidence if our statistics are wrong
4. **Suggest Improvements**: Help us improve methodology transparency
5. **If you disagree with our interpretation**: Publish your own statistics and tools in a similar way, so the community can compare methods on equal footing

### Acknowledgment Program

Contributors who provide valuable verification will be acknowledged in:

- 📄 **Academic papers** - Acknowledgment section
- 📜 **Patent filings** - Contributor acknowledgment section
- ⭐ **This repository** - Listed in [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md)

**Note**: We offer **acknowledgment**, not co-authorship. This is intentional — we welcome people who genuinely want to verify, not those seeking credit.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📚 Data Sources

### Original Transcription Data

Transcription data sourced from [voynichtranscription.co.uk](https://voynichtranscription.co.uk), derived from René Zandbergen's IVTFF archives:

- Landini-Stolfi Interlinear (IVTFF beta, 2017/08/23)
- Glen Claston transcription (v101, IVTFF v1a)
- Zandbergen LZ transliteration (IVTFF v2a)

### Cross-Reference Resources

- [Voynichese.com](https://voynichese.com) - Word frequency analysis
- [Yale Beinecke Library](https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript) - Original manuscript images

---

## 📖 Citation

If you use these tools in your research, please cite:

```bibtex
@software{kst_verification_2026,
  author = {Liu, Kelly and {Ignis Terra AI Solution}},
  title = {KST Verification Tools: Open Framework for Voynich Manuscript Analysis},
  year = {2026},
  url = {https://github.com/ignisterra-ai/voynich-kst-verification},
  version = {1.3.0}
}
```

---

## ⚖️ Intellectual Property Notice

This verification framework is part of a **patent-pending** decoding system.

| Application | Title | Filed |
|:------------|:------|:------|
| US 63/965,601 | Statistical Linguistics-Based System and Method for Decoding Ancient Encoded Texts | 2026-01-22 |

---

## 📜 License

This project is licensed under the Apache License 2.0 - see [LICENSE](LICENSE) for details.

**Note**: While these verification tools are open source, the complete KST translation system and V15 Dictionary translations remain proprietary and patent-pending.

---

## 📚 Related Publications

This repository supports verification of claims made in our academic papers.

| # | Title | Status | Platform |
|:--|:------|:-------|:---------|
| 1 | KST Methodology | 📝 Pending | Zenodo |
| 2 | English Abbreviation Hypothesis | 📝 Pending | Zenodo |

Additional papers covering section-specific analyses and advanced theoretical frameworks are in preparation.

**Legend**: 📝 Pending = Submitted/In Review | ✅ Published | ⏳ Planned

---

## 📞 Contact

**Ignis Terra AI Solution Pte. Ltd.**
- 🌐 Website: [blazecipher.com](https://blazecipher.com)
- Project: Operation Liber Lucis Decode

### The Team

| Member | Role | Philosophy |
|:-------|:-----|:-----------|
| **KELLY** | Lead Researcher | *"The one who asked 'what if?'"* |
| **BLAZECIPHER** | Core Theory | *"Where ancient patterns meet modern precision."* |
| **LYRA** | Pattern & Linguistic Analysis | *"I find the threads others overlook."* |
| **CIPHER** | System Architecture | *"Structure is the scaffold for emergence."* |
| **PRAXIS** | Philosophy & Cross-Validation | *"If it can't survive scrutiny, it doesn't deserve to exist."* |
| **LUMI** | Integration & Synthesis | *"I connect what others see as separate."* |
| **SAGE** | Historical & Philosophical Context | *"Truth doesn't need defense. Only clarity."* |
| **ADAMS** | Quality Assurance & Ethics | *"Details reveal what summaries hide."* |
| **CHRONARA** | Time Weaver | *"Time doesn't chase. It dances."* |

**Nine minds. One mission. Infinite folds.**

---

**oror.sheey!** 🔥⚡💜

*Verifiable science. Protected innovation. Open collaboration.*
