# Apriori — Association Rule Learning

Market basket analysis using the **Apriori algorithm** to discover purchase patterns in transactional data. Given a set of transactions, Apriori finds frequent itemsets and derives association rules of the form *"customers who bought X also bought Y"*.

Implementations are provided in both Python and R.

---

## Methodology

Apriori works by iteratively identifying frequent itemsets and pruning candidates that fall below a minimum support threshold. From those itemsets, association rules are generated and ranked using three key metrics:

| Metric | Definition |
|---|---|
| **Support** | Fraction of transactions containing the itemset: `count(X) / N` |
| **Confidence** | Probability of Y given X: `count(X ∪ Y) / count(X)` |
| **Lift** | Strength of the rule over random chance: `Confidence / Support(Y)` — values > 1 indicate a meaningful association |

**Steps:**

1. Set minimum support and confidence thresholds.
2. Find all itemsets with support ≥ min_support.
3. Generate rules from those itemsets with confidence ≥ min_confidence.
4. Rank rules by descending lift.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3, R |
| 📊 Data handling | pandas |
| ⛏ Algorithm | apyori (Python), arules (R) |
| 📁 Dataset | Market Basket Optimisation (7 501 transactions, 20 item slots) |

---

## 📦 Dependencies

### Python

```
pandas
apyori
```

Install with:

```bash
pip install pandas apyori
```

### R

```r
install.packages("arules")
```

---

## 🚀 How to Run

### Python

```bash
# Make sure the CSV is in the same directory
python apriori.py
```

The script loads `Market_Basket_Optimisation.csv`, mines association rules (min_support=0.003, min_confidence=0.2, min_lift=3), and prints a ranked table of results.

### R

```r
source("apriori.R")
```

The R script reads the CSV as transactions, trains the Apriori model, and displays the top 10 rules sorted by lift.

---

## ⚠️ Known Issues

- The dataset is bundled as a ~47 KB CSV with no header row; column count is fixed at 20.
- Python thresholds (support, confidence, lift) are hardcoded — adjust them in `apriori.py` as needed.
- The R script reads the CSV file twice (once with `read.csv`, once with `read.transactions`); the first read is redundant.

---

## 📄 License

See [LICENSE](LICENSE) for details.
