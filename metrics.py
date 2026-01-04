import numpy as np

def expectancy(trades):
    if not trades:
        return 0

    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t < 0]

    win_rate = len(wins) / len(trades)
    avg_win = np.mean(wins) if wins else 0
    avg_loss = abs(np.mean(losses)) if losses else 0

    return (win_rate * avg_win) - ((1 - win_rate) * avg_loss)


def max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        peak = max(peak, value)
        dd = (peak - value) / peak
        max_dd = max(max_dd, dd)

    return round(max_dd * 100, 2)
