from datetime import datetime
from typing import Tuple

ALLOW_UNIMPLEMENTED_METHODS = True


def unimplemented(message: str = "Class not yet implemented"):
    if not ALLOW_UNIMPLEMENTED_METHODS:
        raise TodoError(message)

class TodoError(BaseException):
    def __init__(self, *args):
        super().__init__(*args)

class DatabaseError(BaseException):
    def __init__(self, *args):
        super().__init__(*args)

class AuthenticationError(DatabaseError):
    def __init__(self, *args):
        super().__init__(*args)

class KodZaproszeniowy:
    def __init__(self, kod: str):
        # todo: validuj kod
        unimplemented()
        self.__kod = kod

    @property
    def value(self):
        return self.__kod

# już hashowane
class Login:
    def __init__(self, login: str):
        # todo: validuj albo generuj login (nie wiem które)
        unimplemented()
        self.__login = login

    @property
    def value(self):
        return self.__login

# już hashowane
class Haslo:
    def __init__(self, haslo: str):
        # todo: validuj albo generuj haslo (nie wiem które)
        unimplemented()
        self.__haslo = haslo

    @property
    def value(self):
        return self.__haslo
    
class Nick:
    def __init__(self, nick: str):
        # todo: validuj albo generuj haslo (nie wiem które)
        unimplemented()
        self.__nick = nick

    @property
    def value(self):
        return self.__nick

class Token:
    def __init__(self, token: str):
        # todo: validuj albo generuj token (nie wiem które)
        unimplemented()
        self.__token = token

    @property
    def value(self):
        return self.__token

class Rola:
    def __init__(self, rola: str):
        # todo: validuj albo generuj rola (nie wiem które)
        unimplemented()
        self.__rola = rola

    @property
    def value(self):
        return self.__rola
    
class Task:
    def __init__(self):
        self.id: int = None
        self.tekst: str = None # ! Encoded
        self.zrobiony: bool = None
        self.pokoj: str = None
        self.deadline: datetime = None
        
        self.canvas: Tuple[float, float] = None