from abc import ABC,abstractmethod

class TaxPayer(ABC):
    def __init__(self,pan):
        self._pan=pan

    @abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self):
        return f'{self._pan}'

