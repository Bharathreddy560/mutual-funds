import pandas as pd

# Load datasets
funds = pd.read_csv("data/raw/01_fund_master.csv")
sharpe = pd.read_csv("reports/sharpe_ratio.csv")

# Merge fund details with Sharpe ratio
recommend_data = funds.merge(
    sharpe,
    on="amfi_code",
    how="left"
)

def recommend_funds(risk_appetite):
    """
    Recommend top 3 funds based on risk appetite and Sharpe ratio.
    """

    mapping = {
        "Low": ["Low", "Moderately Low"],
        "Moderate": ["Moderate"],
        "High": ["High", "Very High"]
    }

    result = (
        recommend_data[
            recommend_data["risk_category"].isin(mapping[risk_appetite])
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return result[
        ["scheme_name", "risk_category", "sharpe_ratio"]
    ]

if __name__ == "__main__":
    risk = input("Enter risk appetite (Low/Moderate/High): ")

    recommendations = recommend_funds(risk)

    print("\nTop 3 recommended funds:\n")
    print(recommendations.to_string(index=False))