class Backtester:
    def __init__(self, capital=100000):
        self.capital = capital
        self.equity_curve = [capital]
        self.trades = []

    def execute_trade(self, pnl):
        self.capital += pnl
        self.trades.append(pnl)
        self.equity_curve.append(self.capital)
