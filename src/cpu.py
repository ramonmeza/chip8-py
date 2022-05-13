from component import Component


class Cpu:

    # variable declarations


    # methods
    def __init__(self, rate: int) -> None:
        Component.__init__(self, rate)
    
    def tick(self) -> None:
        self._fetch()
        self._decode()
        self._execute()

    def _fetch(self) -> None:
        pass

    def _decode(self) -> None:
        pass

    def _execute(self) -> None:
        pass
