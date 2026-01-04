from engine.risk import apply_stop_loss, apply_target

class StraddleStrategy:
    def __init__(
        self,
        strategy_type="LONG",   # LONG or SHORT
        min_iv_rank=60,
        min_dte=10,
        stop_pct=0.5,
        target_pct=1.0
    ):
        self.strategy_type = strategy_type
        self.min_iv_rank = min_iv_rank
        self.min_dte = min_dte
        self.stop_pct = stop_pct
        self.target_pct = target_pct

    def generate_pnl(self, row):
        premium = row['ce_price'] + row['pe_price']
        move = abs(row['spot'] - row['strike'])

        if self.strategy_type == "LONG":
            pnl = move - premium
        else:
            pnl = premium - move

        if apply_stop_loss(pnl, premium, self.stop_pct):
            return -premium * self.stop_pct

        if apply_target(pnl, premium, self.target_pct):
            return premium * self.target_pct

        return pnl
