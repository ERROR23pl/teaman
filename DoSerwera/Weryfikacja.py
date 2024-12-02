import typing

def zweryfikuj(login: str, token: str, nickWeryfikowanego: str, nowaRola: str, kluczeSerweraZaszyfrowaneKluczemWeryfikowanego: typing.Tuple[str,str]) -> typing.Tuple[bool,bool]:   #[czy były uprawnienia, czy był taki użytkownik do zweryfikowania]
    return False,False


def listaNiezweryfikowanych(login: str, token: str) -> typing.Tuple[bool,typing.List[str]]: #[czy były uprawnienia, lista nicków niezweryfikowanych użytkowników]
    return False,[""]