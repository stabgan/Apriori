# Apriori Association Rule Learning
# Market Basket Analysis using the Apriori algorithm

import pandas as pd
from apyori import apriori


def load_transactions(filepath):
    """Load transaction data from CSV and return a list of transactions."""
    dataset = pd.read_csv(filepath, header=None)
    num_rows, num_cols = dataset.shape
    transactions = []
    for i in range(num_rows):
        transaction = [
            str(dataset.values[i, j])
            for j in range(num_cols)
            if str(dataset.values[i, j]) != "nan"
        ]
        transactions.append(transaction)
    return transactions


def format_results(results):
    """Convert apyori results into a readable DataFrame."""
    records = []
    for item in results:
        for rule in item.ordered_statistics:
            lhs = ", ".join(rule.items_base) if rule.items_base else "(all)"
            rhs = ", ".join(rule.items_add)
            records.append({
                "LHS": lhs,
                "RHS": rhs,
                "Support": round(item.support, 4),
                "Confidence": round(rule.confidence, 4),
                "Lift": round(rule.lift, 4),
            })
    df = pd.DataFrame(records)
    if not df.empty:
        df = df.sort_values(by="Lift", ascending=False).reset_index(drop=True)
    return df


def main():
    # Data Preprocessing
    transactions = load_transactions("Market_Basket_Optimisation.csv")

    # Training Apriori on the dataset
    rules = apriori(
        transactions,
        min_support=0.003,
        min_confidence=0.2,
        min_lift=3,
        min_length=2,
    )

    # Visualising the results
    results = list(rules)
    df = format_results(results)
    print(f"Found {len(df)} association rules:\n")
    print(df.to_string(index=True))


if __name__ == "__main__":
    main()
