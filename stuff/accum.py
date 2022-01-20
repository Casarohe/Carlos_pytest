class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more = 1):
        self._count += more


class Accumulator2:
    def __init__(self):
        self._county = 1

    @property
    def county(self):
        return self._county

    def duplicate(self, mult = 2):
        self._county *= mult