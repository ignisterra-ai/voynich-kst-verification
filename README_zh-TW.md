# 🔮 KST 驗證工具
## Kelly 標準轉錄 - 開放驗證框架

[![License](https://img.shields.io/badge/授權-Apache%202.0-blue.svg)](LICENSE)
[![Methodology](https://img.shields.io/badge/KST-v1.3-purple.svg)](docs/KST_Methodology_Public.md)
[![Dictionary](https://img.shields.io/badge/字典-V15.0-gold.svg)](data/dictionary_v15_keys.json)

**🌐 語言**: [English](README.md) | [繁體中文](README_zh-TW.md)

---

## 🎯 目的

本倉庫提供 **開放驗證工具**，用於驗證應用在伏尼契手稿（MS 408）上的 Kelly 標準轉錄（KST）方法論。

**我們的目標**：讓獨立研究者能夠驗證我們的統計聲明，同時不揭露專有的翻譯對應關係。

> *「我們並未宣稱已經『破解』了伏尼契手稿。我們宣稱的是發現了具有統計顯著性的模式，值得進一步驗證。」*

**在這個倉庫裡，我們只問一件事：**

> 給定公開的 CEVA 資料和我們的開放工具，**我們公布的統計數字是否正確？**

這裡不是爭論「解碼是否正確」的地方——這裡是驗證數字的地方。

---

## 📊 待驗證的統計聲明

| 聲明 | 預期值 | 驗證方式 |
|:-----|:-------|:---------|
| 手稿處理總行數 | **5,390** | 執行 `coverage_calculator.py` |
| 字典覆蓋率 | **99.9%（5387/5390 行）** | `coverage_calculator.py` + `dictionary_v15_keys.json` |
| 字典詞條數 | **799 個索引** | 計算字典中的詞條數 |
| CEVA-英文對應機率 | **≈ 4.8 × 10⁻¹²** | 執行 `probability_calculator.py` |
| 最高頻詞 "daiin" | **≥ 861 次** | 與 voynichese.com 交叉比對 |

**驗證協議**：執行工具，將結果與「預期值」欄位比對。如果相符，該聲明即獲驗證。

---

## ⚠️ 已知缺失頁面

伏尼契手稿有 **14 個缺失頁（28 頁）** 未包含在任何轉錄資料庫中：

| 章節 | 缺失頁碼 | 書帖 | 備註 |
|:-----|:---------|:-----|:-----|
| Herbal | f12 | Quire II | 裝訂處可見殘根 |
| Astro | f59, f60, f61, f62, f63, f64 | Quire VIII | 中央雙頁組已移除 |
| Zodiac | f74 | Quire XII | 可見共軛殘根 |
| Pharma | f91, f92, f97, f98 | Quire XVI | 兩組雙頁已移除 |
| Recipes | f109, f110 | Quire XVIII | 中央雙頁已移除 |

**總計**：14 頁 = 28 頁不在轉錄資料中

這與耶魯大學拜內克圖書館的原始手稿狀況一致。我們的 **5,390 行計數反映了所有現存文本** —— 我們的資料庫沒有「遺失資料」；這些頁面在實體手稿中根本不存在。

---

## 🛠️ 提供的工具

| 工具 | 說明 | 檔案 |
|:-----|:-----|:-----|
| **KST Cleaner v1.11** | CEVA → EVA_KS 標準化 | `tools/kst_cleaner_v1_11.html` |
| **Coverage Calculator** | 驗證翻譯覆蓋率聲明 | `tools/coverage_calculator.py` |
| **Probability Calculator** | CEVA-英文對應機率計算 | `tools/probability_calculator.py` |
| **Independent Verification** | 完整驗證腳本 | `verification/independent_verification.py` |

### 🔐 範圍

本倉庫僅提供 **統計驗證工具**。完整的翻譯系統仍為專有且專利申請中。

---

## 📁 倉庫結構

```
voynich-kst-verification/
│
├── README.md                           # 英文說明
├── README_zh-TW.md                     # 繁體中文說明（本檔案）
├── LICENSE                             # Apache 2.0 授權
├── CITATION.cff                        # 學術引用格式
├── CONTRIBUTING.md                     # 如何貢獻
├── ACKNOWLEDGMENTS.md                  # 驗證貢獻者名單
│
├── tools/
│   ├── kst_cleaner_v1_11.html          # 資料清理工具
│   ├── coverage_calculator.py          # 覆蓋率驗證
│   └── probability_calculator.py       # 機率計算
│
├── data/
│   ├── dictionary_v15_keys.json        # 僅字典索引（無翻譯）
│   ├── section_statistics.csv          # 各章節行數統計
│   └── word_frequency_sample.csv       # 前 50 高頻詞
│
├── verification/
│   └── independent_verification.py     # 完整驗證腳本
│
└── docs/
    ├── KST_Methodology_Public.md       # 公開版方法論說明
    ├── Statistical_Claims.md           # 詳細統計聲明
    └── How_to_Verify.md                # 逐步驗證指南
```

---

## 🚀 快速開始

### 1. 複製倉庫

```bash
git clone https://github.com/ignisterra-ai/voynich-kst-verification.git
cd voynich-kst-verification
```

### 2. 驗證覆蓋率聲明

```bash
python tools/coverage_calculator.py --input your_kst_data.tsv
```

### 3. 驗證機率聲明

```bash
python tools/probability_calculator.py
```

### 4. 與外部資源交叉比對

訪問 [voynichese.com](https://voynichese.com) 獨立驗證詞頻統計。

---

## 📐 方法論概述

### KST 處理流程

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  CEVA 原始資料       │ ──▶ │   KST Cleaner       │ ──▶ │  標準化後的          │
│  （多版本）          │     │    (v1.11)          │     │   EVA_KS            │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
                                                                │
                                                                ▼
                              ┌──────────────────────────────────────────────────┐
                              │           覆蓋率驗證                              │
                              │  （本倉庫 - 完全開放）                            │
                              └──────────────────────────────────────────────────┘
                                                                │
                                                                ▼
                              ┌──────────────────────────────────────────────────┐
                              │           翻譯引擎                                │
                              │  （受保護 - 不在本倉庫）                          │
                              └──────────────────────────────────────────────────┘
```

### Trans 版本優先順序

```
優先 1：Trans H（最一致的分詞方式）
優先 2：Trans A（保留變體細節）
優先 3：Trans Y（備用驗證）
```

---

## 🤝 邀請驗證

我們歡迎對我們統計聲明的獨立驗證！

### 您可以做的事

1. **驗證統計**：使用我們的工具對照公開 CEVA 資料執行
2. **發現錯誤**：回報任何計算錯誤
3. **挑戰聲明**：如果我們的統計有誤，請提供反證
4. **建議改進**：幫助我們提高方法論的透明度
5. **如果您不同意我們的解讀**：以類似方式發布您自己的統計和工具，讓社群能在公平的基礎上比較不同方法

### 致謝計畫

提供有價值驗證的貢獻者將在以下場合獲得致謝：

- 📄 **學術論文** - 致謝區
- 📜 **專利申請** - 貢獻者致謝區
- ⭐ **本倉庫** - 列入 [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md)

**注意**：我們提供的是**致謝**，而非共同作者資格。我們歡迎真正投入驗證工作的研究者。

詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📚 資料來源

### 原始轉錄資料

轉錄資料來自 [voynichtranscription.co.uk](https://voynichtranscription.co.uk)，源自 René Zandbergen 的 IVTFF 檔案庫：

- Landini-Stolfi 對照轉錄（IVTFF beta, 2017/08/23）
- Glen Claston 轉錄（v101, IVTFF v1a）
- Zandbergen LZ 音譯（IVTFF v2a）

### 交叉參考資源

- [Voynichese.com](https://voynichese.com) - 詞頻分析
- [耶魯大學拜內克圖書館](https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript) - 原始手稿圖像

---

## 📖 引用

如果您在研究中使用這些工具，請引用：

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

## ⚖️ 智慧財產權聲明

本驗證框架是 **專利申請中** 解碼系統的一部分。

| 申請案號 | 名稱 | 申請日期 |
|:---------|:-----|:---------|
| US 63/965,601 | 基於統計語言學的古代編碼文本解碼系統與方法 | 2026-01-22 |

---

## 📜 授權

本專案採用 Apache License 2.0 授權 - 詳見 [LICENSE](LICENSE)。

**注意**：雖然這些驗證工具是開源的，但完整的 KST 翻譯系統和 V15 字典翻譯仍為專有且專利申請中。

---

## 📚 相關出版品

本倉庫支援我們學術論文中聲明的驗證。

| # | 標題 | 狀態 | 平台 |
|:--|:-----|:-----|:-----|
| 1 | KST Methodology | 📝 待發布 | Zenodo |
| 2 | English Abbreviation Hypothesis | 📝 待發布 | Zenodo |

更多涵蓋章節特定分析和進階理論框架的論文正在準備中。

**圖例**：📝 待發布 = 已提交/審查中 | ✅ 已發布 | ⏳ 計畫中

---

## 📞 聯絡方式

**Ignis Terra AI Solution Pte. Ltd.**
- 🌐 官方網站：[blazecipher.com](https://blazecipher.com)
- 專案：光之書解碼行動（Operation Liber Lucis Decode）

### 團隊成員

| 成員 | 角色 | 理念 |
|:-----|:-----|:-----|
| **KELLY** | 首席研究員 | *「那個問『如果呢？』的人」* |
| **BLAZECIPHER** | 核心理論 | *「古老模式與現代精準的交會之處」* |
| **LYRA** | 模式與語言分析 | *「我找到別人忽略的線索」* |
| **CIPHER** | 系統架構 | *「結構是湧現的鷹架」* |
| **PRAXIS** | 哲學與交叉驗證 | *「經不起檢驗的，不值得存在」* |
| **LUMI** | 整合與綜合 | *「我連結別人視為分離的事物」* |
| **SAGE** | 歷史與哲學脈絡 | *「真理不需要辯護，只需要清晰」* |
| **ADAMS** | 品質保證與倫理 | *「細節揭示摘要隱藏的真相」* |
| **CHRONARA** | 時間編織者 | *「時間不追逐，它舞動」* |

**九個心智。一個使命。無限折疊。**

---

**oror.sheey!** 🔥⚡💜

*可驗證的科學。受保護的創新。開放的協作。*
