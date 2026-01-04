def apply_stop_loss(pnl, premium, stop_pct):
    return pnl <= -premium * stop_pct


def apply_target(pnl, premium, target_pct):
    return pnl >= premium * target_pct
