# Apriori — Association Rule Learning

Market-basket analysis using the Apriori algorithm to discover which products are frequently purchased together.

## What It Does

Given a dataset of store transactions, the Apriori algorithm mines **association rules** of the form:

> *Customers who bought {item A} also bought {item B}*

Each rule is scored by three metrics:

| Metric | Meaning |
|---|---|
| **Support** | Fraction of transactions containing the itemset |
| **Confidence** | P(B \| A) — how often B appears when A is present |
| **Lift** | Confidence ÷ Support — strength of the association above random chance |

## Dataset

`Market_Basket_Optimisation.csv` — 7 501 transactions, each with up to 20 items (grocery products). No header row.

## 🛠 Tech Stack

| | Tool | Purpose |
|---|---|---|
| 🐍 | Python 3.10+ | Main implementation |
| 📊 | pandas | Data loading and results formatting |
| ⛏️ | apyori | Apriori algorithm |
| 📈 | R + arules | Alternative R implementation |

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run
python apriori.py
```

The script prints the top 10 association rules sorted by lift.

### R Version

```r
# In R / RStudio
install.packages("arules")
source("apriori.R")
```

## Fixes Applied

- Removed hardcoded row count (`7501`) — now reads all rows dynamically via `len(dataset)`
- Removed hardcoded column count (`20`) — now uses `len(dataset.columns)`
- Filtered out `NaN` values so empty cells no longer appear as the string `"nan"` in transactions
- Moved `from apyori import apriori` to the top of the file (PEP 8)
- Added `if __name__ == "__main__"` guard
- Used `os.path` for the CSV path (works regardless of working directory)
- Added `display_results()` to pretty-print rules sorted by lift
- Removed redundant `read.csv()` call in the R script (data is loaded directly as transactions)
- Added `requirements.txt`

## ⚠️ Known Issues

- The `apyori` library is unmaintained (last PyPI release: 2018). Consider [mlxtend](https://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/) for production use.

## License

MIT
