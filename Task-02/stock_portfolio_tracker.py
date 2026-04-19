"""
CodeAlpha Internship — Task 2: Stock Portfolio Tracker
Author  : Kosar Bibi
GitHub  : CodeAlpha_StockPortfolioTracker
"""

import csv
import os
from datetime import datetime

# ── Hardcoded stock prices (USD) ─────────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple
    "TSLA":  250.00,   # Tesla
    "GOOGL": 140.00,   # Alphabet (Google)
    "AMZN":  185.00,   # Amazon
    "MSFT":  380.00,   # Microsoft
    "META":  490.00,   # Meta (Facebook)
    "NVDA":  870.00,   # NVIDIA
    "NFLX":  620.00,   # Netflix
}

DIVIDER = "=" * 55


def show_available_stocks() -> None:
    """Print available stocks and their current prices."""
    print(f"\n{'Symbol':<10} {'Company / Stock':<25} {'Price (USD)':>10}")
    print("-" * 50)
    labels = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Alphabet (Google)",
        "AMZN": "Amazon", "MSFT": "Microsoft", "META": "Meta",
        "NVDA": "NVIDIA", "NFLX": "Netflix",
    }
    for sym, price in STOCK_PRICES.items():
        print(f"{sym:<10} {labels[sym]:<25} ${price:>9.2f}")
    print()


def get_portfolio_from_user() -> dict:
    """
    Interactively ask the user which stocks and quantities they hold.
    Returns a dict: {symbol: quantity}
    """
    portfolio = {}
    print("\nEnter your stock holdings (type 'done' when finished).")
    show_available_stocks()

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if not portfolio:
                print("⚠  You haven't added any stocks yet. Please add at least one.")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"⚠  '{symbol}' is not in our list. Available: {', '.join(STOCK_PRICES)}")
            continue

        try:
            qty = int(input(f"   Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("⚠  Quantity must be a positive integer.")
                continue
        except ValueError:
            print("⚠  Invalid quantity. Please enter a whole number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"   Updated {symbol} total to {portfolio[symbol]} shares.")
        else:
            portfolio[symbol] = qty
            print(f"   ✅ {symbol} added.")

    return portfolio


def calculate_portfolio(portfolio: dict) -> list[dict]:
    """Return a list of rows with value calculations."""
    rows = []
    for symbol, qty in portfolio.items():
        price      = STOCK_PRICES[symbol]
        investment = price * qty
        rows.append({
            "Symbol"    : symbol,
            "Quantity"  : qty,
            "Price (USD)": price,
            "Value (USD)": investment,
        })
    return rows


def display_summary(rows: list[dict]) -> float:
    """Pretty-print the portfolio table and return the grand total."""
    print(f"\n{DIVIDER}")
    print("         📊 YOUR STOCK PORTFOLIO SUMMARY")
    print(DIVIDER)
    print(f"{'Symbol':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}")
    print("-" * 42)

    total = 0.0
    for r in rows:
        print(
            f"{r['Symbol']:<8} {r['Quantity']:>6}  "
            f"${r['Price (USD)']:>9.2f}  ${r['Value (USD)']:>11.2f}"
        )
        total += r["Value (USD)"]

    print("-" * 42)
    print(f"{'TOTAL INVESTMENT':>28}  ${total:>11.2f}")
    print(DIVIDER)
    return total


def save_to_txt(rows: list[dict], total: float, filename: str = "portfolio_report.txt") -> None:
    """Save the portfolio to a plain-text file."""
    path = os.path.join(os.getcwd(), filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "w") as f:
        f.write("CodeAlpha — Stock Portfolio Report\n")
        f.write(f"Generated: {timestamp}\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}\n")
        f.write("-" * 41 + "\n")
        for r in rows:
            f.write(
                f"{r['Symbol']:<8} {r['Quantity']:>6}  "
                f"${r['Price (USD)']:>9.2f}  ${r['Value (USD)']:>11.2f}\n"
            )
        f.write("-" * 41 + "\n")
        f.write(f"{'TOTAL':<28}  ${total:>11.2f}\n")

    print(f"\n✅ Report saved to: {path}")


def save_to_csv(rows: list[dict], total: float, filename: str = "portfolio_report.csv") -> None:
    """Save the portfolio to a CSV file."""
    path = os.path.join(os.getcwd(), filename)
    fieldnames = ["Symbol", "Quantity", "Price (USD)", "Value (USD)"]

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        # Append total row
        writer.writerow({
            "Symbol": "TOTAL", "Quantity": "",
            "Price (USD)": "", "Value (USD)": round(total, 2)
        })

    print(f"✅ CSV  saved to: {path}")


def main() -> None:
    print(DIVIDER)
    print("   💹 CodeAlpha Stock Portfolio Tracker")
    print(DIVIDER)

    portfolio = get_portfolio_from_user()
    rows      = calculate_portfolio(portfolio)
    total     = display_summary(rows)

    # Optional: save report
    print("\nWould you like to save your report?")
    print("  1 — Save as .txt")
    print("  2 — Save as .csv")
    print("  3 — Save both")
    print("  4 — No, skip")

    choice = input("Your choice (1/2/3/4): ").strip()
    if choice == "1":
        save_to_txt(rows, total)
    elif choice == "2":
        save_to_csv(rows, total)
    elif choice == "3":
        save_to_txt(rows, total)
        save_to_csv(rows, total)
    else:
        print("No file saved. Goodbye! 👋")


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
