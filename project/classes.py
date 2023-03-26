from abc import (ABC, abstractmethod)
from typing import Union
from datetime import datetime
from random import randint

NOW = datetime.now().strftime("%d-%m-%Y")


class Bank(ABC):

    @abstractmethod
    def __init__(self, name: str, date: str, location: str):
        self.name = name
        self.date = date
        self.location = location

    @abstractmethod
    def getter(self) -> list:
        data = [self.name, self.date, self.location]
        return data


class Central(Bank):
    def __init__(self, name: str, rate: float, date: str = NOW, location: str = "Moscow"):
        super().__init__(name=name, date=date, location=location)
        self.rate = rate

    def getter(self) -> tuple:
        data = super().getter()
        data.insert(0, 'Central')
        data.append(self.rate)
        return tuple(data)

    def issue_license(id: int) -> Union[int, bool]:
        ha_ha = randint(0, 10000)
        if id == ha_ha:
            return ha_ha
        print('u fool')
        return False


class Commercial(Bank, ABC):
    @abstractmethod
    def __init__(self, name: str, license: int, equity: float, date: str, location: str, type: str):
        super().__init__(name=name, date=date, location=location)
        self.license = license
        self.equity = equity
        self.type = type

    @abstractmethod
    def getter(self) -> list:
        data = super().getter()
        data.append(self.type)
        data.append(self.license)
        data.append(self.equity)
        return data

    @abstractmethod
    def run_transaction(self):
        pass


class Universal(Commercial):
    def __init__(self, name: str, license: int, equity: float, date: str = NOW, location: str = "Moscow",
                 type: str = "PJSC"):
        super().__init__(name=name, license=license, equity=equity, date=date, location=location, type=type)

    def getter(self) -> tuple:
        data = super().getter()
        data.insert(0, "Universal")
        return tuple(data)

    @staticmethod
    def issue_loan() -> bool:
        return True

    @staticmethod
    def create_deposit() -> bool:
        return True

    def run_transaction(self) -> bool:
        return True


class Specialized(Commercial, ABC):
    @abstractmethod
    def __init__(self, name: str, license: int, equity: float, date: str = NOW, location: str = "Moscow",
                 type: str = "PJSC", specialization: str = "Credit"):
        super().__init__(name=name, license=license, equity=equity, date=date, location=location, type=type)
        self.specialization = specialization

    @abstractmethod
    def run_transaction(self) -> bool:
        return True
