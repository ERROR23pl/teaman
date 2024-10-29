import typing

def analizaTrueFalse(odpowiedz: bytes) -> bool:         #TODO
    #zmiana odpowiedzi serwera w False lub True
    return True    #tymczasowo


def analizaBoolStr(odpowiedz: bytes) -> typing.Tuple[bool, str]:                    #TODO
    #zmiana odpowiedzi serwera w [False,""] lub [True, odszyfrowany token sesji]
    return [False,""]    #tymczasowo


def analizaBool2Str(odpowiedz: bytes) -> typing.Tuple[bool, str, str]:                    #TODO
    #zmiana odpowiedzi serwera w [False,"",""] lub [True, odszyfrowany token sesji, rola]
    return [False,"",""]    #tymczasowo

