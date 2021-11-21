class TableRollResult():
    """!
    This Class represent the roll result on a table.
    """
    def __init__(self, rollresult:dict = {}) -> None:
        self._rollresult = rollresult

    def getRollresult(self) -> dict:
        return self._rollresult