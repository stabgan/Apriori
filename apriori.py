# Apriori — Association Rule Learning
# Discovers frequent itemsets in transaction data using the Apriori algorithm.

import os

import numpy as np
import pandas as pd
from apyori import apriori


def load_transactions(csv_path: str) -> list[list[str]]:
    """Load transaction data from a CSV file, filtering out empty (NaN) cells."""
    dataset = pd.read_csv(csv_path, header=None)
    transactions = []
    for i in range(len(dataset)):
        transaction = [
            str(dataset.values[i, j])
            for j in range(len(dataset.columns))
            if pd.notna(dataset.values[i, j])
        ]
        transactions.append(transaction)
    return transactions


def run_apriori(
    transactions: list[list[str]],
    min_support: float = 0.003,
    min_confidence: float = 0.2,
    min_lift: int = 3,
    min_length: int = 2,
) -> list:
    """Run the Apriori algorithm and return the raw results."""
    rules = apriori(
        transactions,
        min_support=min_support,
        min_confidence=min_confidence,
        min_lift=min_lift,
        min_length=min_length,
    )
    return list(rules)


def display_results(results: list, top_n: int = 10) -> None:
    """Pretty-print the top association rules sorted by lift."""
    if not results:
        print("No association rules found with the given thresholds.")
        return

    rows = []
    for item in results:
        for rule in item.ordered_statistics:
            rows.append(
                {
                    "LHS": ", ".join(rule.items_base) or "(all)",
                    "RHS": ", ".join(rule.items_add),
                    "Support": round(item.support, 4),
                    "Confidence": round(rule.confidence, 4),
                    "Lift": round(rule.lift, 4),
                }
            )

    df = pd.DataFrame(rows)
    df.sort_values("Lift", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df.head(top_n).to_string(index=False))


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Market_Basket_Optimisation.csv")

    transactions = load_transactions(csv_path)
    results = run_apriori(transactions)
    print(f"\nFound {len(results)} association rules.\n")
    display_results(results)
