import pandas as pd

from ...core import History, Strategy


class RandomForestStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def fit(self, history: History):
        pass

    def execute(
        self, idx, position: pd.Series, history: History
    ) -> pd.Series:  # expected element type: Signal
        pass
