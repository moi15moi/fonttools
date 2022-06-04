from fontTools.ttLib.tables.sortNamesStrategy.AbstractSortStrategy import AbstractSortStrategy
from typing import List

class FontConfigStrategy(AbstractSortStrategy):

    # From	https://gitlab.freedesktop.org/fontconfig/fontconfig/-/blob/d863f6778915f7dd224c98c814247ec292904e30/src/fcfreetype.c#L1078
    #		https://github.com/freetype/freetype/blob/b98dd169a1823485e35b3007ce707a6712dcd525/include/freetype/ttnameid.h#L86-L91
    PLATFORM_ID_APPLE_UNICODE = 0
    PLATFORM_ID_MACINTOSH = 1
    PLATFORM_ID_ISO = 2
    PLATFORM_ID_MICROSOFT = 3
    PLATFORM_ID_ORDER = [
        PLATFORM_ID_MICROSOFT,
        PLATFORM_ID_APPLE_UNICODE,
        PLATFORM_ID_MACINTOSH,
        PLATFORM_ID_ISO,
    ]

    def isEnglish(self, name):
        # From https://gitlab.freedesktop.org/fontconfig/fontconfig/-/blob/d863f6778915f7dd224c98c814247ec292904e30/src/fcfreetype.c#L1111-1125
        return (name.platformID, name.langID) in ((1, 0), (3, 0x409))

    def getDebugName(self, nameID: int, names: List) -> str:
        names = sorted(names, key=lambda name: (self.PLATFORM_ID_ORDER.index(name.platformID), name.nameID, name.platEncID, -self.isEnglish(name), name.langID))

        for name in names:
            if name.nameID != nameID:
                continue
            try:
                unistr = name.toUnicode()
            except UnicodeDecodeError:
                continue

            return unistr