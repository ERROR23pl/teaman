import typing
import ManagerNazw as Nazwy
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerKluczy as Klucze

class Task:  
    def __init__(self, idTaska: int, nazwaTaska: str, data: typing.Tuple[int,int,int], koordynaty: typing.Tuple[float,float], listaZaleznosci: typing.List[int]):        
        if(Nazwy.przetestujNazwe(nazwaTaska)):
            self.id: int = idTaska
            self.nazwa: str = nazwaTaska
            self.dzien: int = data[0]
            self.miesiac: int = data[1]
            self.rok: int = data[2]
            self.x: float = koordynaty[0]
            self.y: float = koordynaty[1]
            self.wymaganeTaski: typing.List[int] = listaZaleznosci
        else:
            raise NameError("")
        
    def get_date(self) -> str:
        return str(self.rok)+"-"+str(self.miesiac)+"-"+str(self.dzien)


class Wiadomosc:
    def __init__(self,kodDaty: typing.List[int], trescWiadomosci: str = ""):
        if(type(kodDaty)==int):
            self.data = kodDaty
        else:
            dataDzienna = str(kodDaty[0])
            if(kodDaty[1]>=10):
                dataDzienna=dataDzienna+"-"+str(kodDaty[1])
            else:
                dataDzienna=dataDzienna+"-0"+str(kodDaty[1])
            if(kodDaty[2]>=10):
                dataDzienna=dataDzienna+"-"+str(kodDaty[2])
            else:
                dataDzienna=dataDzienna+"-0"+str(kodDaty[2])
            self.data = dataDzienna
            
            if(kodDaty[3]>=10):
                czas=str(kodDaty[3])
            else:
                czas="0"+str(kodDaty[3])
            if(kodDaty[4]>=10):
                czas=czas+":"+str(kodDaty[4])
            else:
                czas=czas+":0"+str(kodDaty[4])
            if(kodDaty[5]>=10):
                czas=czas+":"+str(kodDaty[5])
            else:
                czas=czas+":0"+str(kodDaty[5])
            self.czas = czas
        self.tresc: str = Nazwy.zabezpieczCudzyslowy(trescWiadomosci)
        

class WpisKalendarza:
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


class rola:        # rola użytkownika
    def __init__(self, dane: str):
        if(Nazwy.przetestujRole(dane)):
            self.wart: str = dane
        else:
            raise NameError("")