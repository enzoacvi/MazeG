from strategies import Strategy


class Generator:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self.s = None
        self.n = None

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy: Strategy):
        self._strategy = new_strategy

    def generate(self, size: int):
        return self._strategy.construct(size, s=self.s, n=self.n)
