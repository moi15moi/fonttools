from abc import ABC, abstractmethod
from typing import List


class AbstractSortStrategy(ABC):

    @abstractmethod
    def getDebugName(self, nameID: int, names: List) -> str:
        pass