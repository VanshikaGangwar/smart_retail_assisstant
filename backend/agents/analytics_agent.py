import pandas as pd

# Load dataset
df = pd.read_csv("data/sales.csv")

def analytics_agent(question):

    question = question.lower()

    # ----------------------------------------
    # TOTAL SALES
    # ----------------------------------------

    if "total sales" in question:

        total_sales = df['Weekly_Sales'].sum()

        return f"""
Total Sales: {total_sales:.2f}
"""

    # ----------------------------------------
    # AVERAGE SALES
    # ----------------------------------------

    elif "average weekly sales" in question:

        avg_sales = df['Weekly_Sales'].mean()

        return f"""
Average Weekly Sales: {avg_sales:.2f}
"""

    # ----------------------------------------
    # BEST STORE
    # ----------------------------------------

    elif (
        "highest weekly sales" in question
        or "best performing store" in question
    ):

        top_store = (
            df.groupby('Store')['Weekly_Sales']
            .sum()
            .idxmax()
        )

        top_sales = (
            df.groupby('Store')['Weekly_Sales']
            .sum()
            .max()
        )

        return f"""
Best Performing Store: {top_store}

Total Sales: {top_sales:.2f}
"""

    # ----------------------------------------
    # TOP 5 STORES
    # ----------------------------------------

    elif "top 5 stores" in question:

        top_stores = (
            df.groupby('Store')['Weekly_Sales']
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        response = "Top 5 Stores By Sales:\n\n"

        for store, sales in top_stores.items():

            response += (
                f"Store {store}: "
                f"{sales:.2f}\n"
            )

        return response

    # ----------------------------------------
    # LOWEST SALES STORE
    # ----------------------------------------

    elif "lowest weekly sales" in question:

        low_store = (
            df.groupby('Store')['Weekly_Sales']
            .sum()
            .idxmin()
        )

        low_sales = (
            df.groupby('Store')['Weekly_Sales']
            .sum()
            .min()
        )

        return f"""
Lowest Performing Store: {low_store}

Total Sales: {low_sales:.2f}
"""

    # ----------------------------------------
    # HOLIDAY ANALYSIS
    # ----------------------------------------

    elif "holiday" in question:

        holiday_sales = (
            df[df['Holiday_Flag'] == 1]
            ['Weekly_Sales']
            .mean()
        )

        non_holiday_sales = (
            df[df['Holiday_Flag'] == 0]
            ['Weekly_Sales']
            .mean()
        )

        return f"""
Average Holiday Sales: {holiday_sales:.2f}

Average Non-Holiday Sales: {non_holiday_sales:.2f}
"""

    # ----------------------------------------
    # SALES TREND
    # ----------------------------------------

    elif "sales trend" in question:

        trend = (
            df.groupby('Date')['Weekly_Sales']
            .sum()
            .tail(5)
        )

        response = "Recent Sales Trend:\n\n"

        for date, sales in trend.items():

            response += (
                f"{date}: "
                f"{sales:.2f}\n"
            )

        return response

    # ----------------------------------------
    # DEFAULT RESPONSE
    # ----------------------------------------

    else:

        return """
Analytics question not recognized.

Try asking:
- Total sales
- Top 5 stores
- Best performing store
- Holiday sales
- Sales trend
"""