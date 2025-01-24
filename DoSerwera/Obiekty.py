import typing
import DoSerwera.ManagerNazw as Nazwy
import DoSerwera.ManagerHasel as Hasla
import DoSerwera.ManagerKodow as Kody
import DoSerwera.ManagerKluczy as Klucze

class Task:
    def __init__(self, idTaska: int, czyUkonczony: bool, nazwaTaska: str, data: typing.Tuple[int,int,int], koordynaty: typing.Tuple[float,float], listaZaleznosci: typing.List[int]):
        if(Nazwy.przetestujNazwe(nazwaTaska)):
            self.id: int = idTaska
            self.ukonczony: bool = czyUkonczony
            self.nazwa: str = nazwaTaska
            self.dzien: int = data[0]
            self.miesiac: int = data[1]
            self.rok: int = data[2]
            self.x: float = koordynaty[0]
            self.y: float = koordynaty[1]
            self.wymaganeTaski: typing.List[int] = listaZaleznosci
        else:
            raise NameError("")


class Wiadomosc:
    def __init__(self,kodDaty: int, czyMaBycAutor: bool, trescWiadomosci: str = "", autorWiadomosci: str = ""):
        if((not czyMaBycAutor) or Nazwy.przetestujNazwe(autorWiadomosci)):
            self.data: int = kodDaty
            self.tresc: str = Nazwy.zabezpieczCudzyslowy(trescWiadomosci)
            self.autor: str = autorWiadomosci
        else:
            raise NameError("")
        

class WpisKalendarza:
    @classmethod
    def from_date_str(nazwaWpisu: str, data: str):
        daneDaty = str.split(data,"-")
        return WpisKalendarza(nazwaWpisu, daneDaty[2], daneDaty[1], daneDaty[0])
    
    def __init__(self,nazwaWpisu: str, data: typing.Tuple[int,int,int]):
        self.nazwa: str = Nazwy.zabezpieczCudzyslowy(nazwaWpisu)
        self.dzien: int = data[0]
        self.miesiac: int = data[1]
        self.rok: int = data[2]

    def get_date(self) -> str:
        return str(self.rok)+"-"+str(self.miesiac)+"-"+str(self.dzien)


class nazwa:        # nazwa projektu lub pokoju, login, nick
    def __init__(self, dane: str):
        if(Nazwy.przetestujNazwe(dane)):
            self.wart: str = dane
        else:
            raise NameError("")


class haslo:
    def __init__(self, dane: str):
        if(Hasla.poprawnoscHasla(dane)):
            self.wart: str = dane
        else:
            raise NameError("")


class kod:                          # kod zaproszeniowy lub token
    def __init__(self, dane: str):
        if(Kody.przetestujKod(dane)):
            self.wart: str = dane
        else:
            raise NameError("")


class klucz:
    def __init__(self, dane: str):
        if(Klucze.testPoprawnosciKlucza(dane)):
            self.wart: str = dane
        else:
            raise NameError("")


class nazwaPliku:        # nazwa pliku
    def __init__(self, dane: str):
        if(Nazwy.przetestujNazwePliku(dane)):
            self.wart: str = dane
        else:
            raise NameError("")

class hash:        # hash
    def __init__(self, dane: str):
        if(Nazwy.przetestujHash(dane)):
            self.wart: str = dane
        else:
            raise NameError("")