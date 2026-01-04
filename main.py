import pandas as pd
from engine.backtester import Backtester
from engine.metrics import expectancy, max_drawdown
from strategy.straddle import StraddleStrategy

# Load data
options = pd.read_csv("data/options_data.csv")
iv = pd.read_csv("data/iv_data.csv")
data = options.merge(iv, on="date")

# Initialize
bt = Backtester(capital=100000)
strategy = StraddleStrategy(
    strategy_type="SHORT",
    min_iv_rank=65,
    min_dte=15,
    stop_pct=0.4,
    target_pct=0.8
)

# Run backtest
for _, row in data.iterrows():
    if row['iv_rank'] < strategy.min_iv_rank or row['dte'] < strategy.min_dte:
        continue

    pnl = strategy.generate_pnl(row)
    bt.execute_trade(pnl)

# Results
print("Total Trades:", len(bt.trades))
print("Expectancy:", round(expectancy(bt.trades), 2))
print("Max Drawdown (%):", max_drawdown(bt.equity_curve))
print("Final Capital:", bt.capital)
