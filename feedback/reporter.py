"""Generate textual reports from analysis."""


def report(analysis):
    return "\n".join(f"{k}: {v}" for k, v in analysis.items())
