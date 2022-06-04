from fontTools.ttLib.tables.sortNamesStrategy.AbstractSortStrategy import AbstractSortStrategy
from typing import List

class DefaultStrategy(AbstractSortStrategy):

    def getDebugName(self, nameID: int, names: List) -> str:
        englishName = someName = None
        for name in names:
            if name.nameID != nameID:
                continue
            try:
                unistr = name.toUnicode()
            except UnicodeDecodeError:
                continue

            someName = unistr
            if (name.platformID, name.langID) in ((1, 0), (3, 0x409)):
                englishName = unistr
                break
        if englishName:
            return englishName
        elif someName:
            return someName
        else:
            return None