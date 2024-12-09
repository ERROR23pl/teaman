import ManagerPlikowKomunikacyjnych as Pliki
import ManagerHasel as Hasla
import ManagerKodow as Kody
import ManagerNazw as Nazwy
import ManagerKluczy as Klucze
import LaczenieZProjektem as LogIRej
import WlasnyProjekt as WlProj
#import KomunikacjaZBaza as Bazy
import MockTestowyKomunikacjiZBaza as Bazy
import ZarzadzaniePokojami as Pokoje
import ZarzadzanieCzlonkamiPokojow as CzlPokojow
import ZarzadzanieTaskami as Taski
import ZarzadzanieChatami as Chaty
import ZarzadzanieKalendarzem as Kalendarz
import UdostepnianiePlikow as udPlikow
import WeryfikacjaIRole as Wer
import typing
import hashlib as hash


#TODO plik w rozwoju; po zakończeniu, przerzucić case'y do osobnych plików, a tu tylko wywołania

def ObsluzZapytanie(plikKomunikacyjny):
    try:
        zapytanie: typing.List = Pliki.analizaPliku(plikKomunikacyjny)
        operacja: str = str(zapytanie[0])
        nazwaProjektu: str = str(zapytanie[1])
        
        if(not Nazwy.przetestujNazwe(nazwaProjektu)):
            return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa projektu nie spełnia założeń"])   #niepoprawna nazwa projektu
        
        
        if(operacja=="logowanie"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            haslo: str = str(zapytanie[3])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaLogowania(login,haslo)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="rejestracja"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            kodZapr: str = str(zapytanie[2])
            login: str = str(zapytanie[3])
            haslo: str = str(zapytanie[4])
            nick: str = str(zapytanie[5])
            
            if((not Kody.przetestujKod(kodZapr))  or (not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo)) or (not Nazwy.przetestujNazwe(nick))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(login==hash.sha3_512(nick.encode()).hexdigest()):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaRejestracji(nazwaProjektu,kodZapr,login,haslo,nick)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="tworzenie projektu"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt istnieje"])   #nie można stworzyć projektu, bo już istnieje
            
            login: str = str(zapytanie[2])
            haslo: str = str(zapytanie[3])
            nick: str = str(zapytanie[4])
            kluczPub: str = str(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Hasla.poprawnoscHasla(haslo)) or (not Nazwy.przetestujNazwe(nick)) or(not Klucze.testPoprawnosciKlucza(kluczPub))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(login==hash.sha3_512(nick.encode()).hexdigest()):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.stworzProjekt(nazwaProjektu,login,haslo,nick,kluczPub)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="zapraszanie"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            kodZapr: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if((not Kody.przetestujKod(kodZapr))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy kod"])   #niepoprawny kod - prośba o nowy
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.dodajZaproszenie(login,token,kodZapr)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie projektu"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.usunProjekt(nazwaProjektu,login,token)
            
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="tworzenie pokoju"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if((not Nazwy.przetestujNazwe(nazwaPokoju))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa projektu nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.stworzPokoj(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie pokoju"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            if(nazwaProjektu==nazwaPokoju):
                return Pliki.stworzPlikZOdpowiedzia(False, dane=["Nie można usunąć pokoju głównego"])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if((not Nazwy.przetestujNazwe(nazwaPokoju))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.usunPokoj(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie do pokoju"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            dodawanyUzytkownik: str = str(zapytanie[5])
            kluczePokojuZaszyfrowaneKluczemDodawanego: typing.Tuple[str,str] = [str(zapytanie[6]),str(zapytanie[7])]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwe(dodawanyUzytkownik)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick dodawanego użytkownika
            
            rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.dodajDoPokoju(login,token,nazwaPokoju,dodawanyUzytkownik,kluczePokojuZaszyfrowaneKluczemDodawanego)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie z pokoju"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            usuwanyUzytkownik: str = str(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwe(usuwanyUzytkownik)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick usuwanego użytkownika
            
            rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.usunZPokoju(login,token,nazwaPokoju,usuwanyUzytkownik)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="lista pokojow"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.listaPokojow(login,token)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="modyfikacja taskow"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            dodawaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[5]
            usuwaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[6]
            modyfikowaneTaski: typing.List[typing.Tuple[int,str,typing.Tuple[int,int,int],typing.Tuple[float,float],typing.List[int]]] = zapytanie[7]
            
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            i: int = 0
            while(i<len(dodawaneTaski)):
                if(Nazwy.przetestujNazwe(dodawaneTaski[i][1])):
                    i+=1
                else:
                    if(i<len(dodawaneTaski)):
                        dodawaneTaski=dodawaneTaski[:i]+dodawaneTaski[i+1:]
                    else:
                        dodawaneTaski=dodawaneTaski[:i]

            i=0
            while(i<len(usuwaneTaski)):
                if(Nazwy.przetestujNazwe(usuwaneTaski[i][1])):
                    i+=1
                else:
                    if(i<len(usuwaneTaski)):
                        usuwaneTaski=usuwaneTaski[:i]+usuwaneTaski[i+1:]
                    else:
                        usuwaneTaski=usuwaneTaski[:i]
            
            i=0
            while(i<len(modyfikowaneTaski)):
                if(Nazwy.przetestujNazwe(modyfikowaneTaski[i][1])):
                    i+=1
                else:
                    if(i<len(modyfikowaneTaski)):
                        modyfikowaneTaski=modyfikowaneTaski[:i]+modyfikowaneTaski[i+1:]
                    else:
                        modyfikowaneTaski=modyfikowaneTaski[:i]
                    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.obslugaTaskow(login,token,nazwaPokoju,[dodawaneTaski,usuwaneTaski,modyfikowaneTaski])
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="pobierz taski"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.pobierzTaski(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="zaznacz task"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            idTaska: int = int(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoWykonany(login,token,nazwaPokoju,idTaska)
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="odznacz task"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            idTaska: int = int(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoNiewykonany(login,token,nazwaPokoju,idTaska)
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login,token,nazwaPokoju))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobierz chat"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.pobierzChat(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="zaktualizuj chat"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            ostatniaPosiadana: typing.Tuple[str,int] = [str(zapytanie[5]),int(zapytanie[6])]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwe(zapytanie[5])):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick autora ostatniej wiadomości   
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.zaktualizujChat(login,token,nazwaPokoju,ostatniaPosiadana)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="wyslij wiadomosc"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            ostatniaPosiadana: typing.Tuple[str,int] = [str(zapytanie[5]),int(zapytanie[6])]
            wiadomosc: typing.Tuple[str,int] = [str(zapytanie[7]),int(zapytanie[8])]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwe(zapytanie[5])):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick autora ostatniej wiadomości  
            
            wiadomosc[0]=Nazwy.zabezpieczCudzyslowy(wiadomosc[0])
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.wyslijWiadomosc(login,token,nazwaPokoju,ostatniaPosiadana,wiadomosc)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobierz kalendarz"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])   
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.pobierzKalendarz(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie wpisu kalendarza"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [str(zapytanie[5]),zapytanie[6]]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.dodajDoKalendarza(login,token,nazwaPokoju,wpis)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie wpisu kalendarza"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [str(zapytanie[5]),zapytanie[6]]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.usunZKalendarza(login,token,nazwaPokoju,wpis)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="modyfikacja wpisu kalendarza"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            wpis: typing.Tuple[str,typing.Tuple[int,int,int]] = [str(zapytanie[5]),zapytanie[6]]
            noweDane: typing.Tuple[str,typing.Tuple[int,int,int]] = [str(zapytanie[7]),zapytanie[8]]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis[0]=Nazwy.zabezpieczCudzyslowy(wpis[0])
            noweDane[0]=Nazwy.zabezpieczCudzyslowy(noweDane[0])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.modyfikujWpisKalendarza(login,token,nazwaPokoju,wpis,noweDane)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie pliku"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            nazwaPliku: str = str(zapytanie[5])
            zawartoscPliku: bytes = (str(zapytanie[6])).encode()
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwePliku(nazwaPliku)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa pliku
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.dodajPlik(login,token,nazwaPokoju,nazwaPliku,zawartoscPliku)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie pliku"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            nazwaPliku: str = str(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwePliku(nazwaPliku)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa plikuu
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.usunPlik(login,token,nazwaPokoju,nazwaPliku)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobranie pliku"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            nazwaPliku: str = str(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(not Nazwy.przetestujNazwePliku(nazwaPliku)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa pliku
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzPlik(login,token,nazwaPokoju,nazwaPliku)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobranie listy plikow"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nazwaPokoju: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nazwaPokoju)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzListePlikow(login,token,nazwaPokoju)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="ustawianie klucza"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            kluczPub: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if((not Klucze.testPoprawnosciKlucza(kluczPub))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy klucz"])   #niepoprawny klucz - prośba o nowy
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaUstawieniaKluczaPublicznego(login,token,kluczPub)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobieranie klucza uzytkownika"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nickUzytkownika: str = str(zapytanie[4])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token)) or (not Nazwy.przetestujNazwe(nickUzytkownika))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.pobierzKluczPublicznyUzytkownika(login,token,nickUzytkownika)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="lista niezweryfikowanych"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.listaNiezweryfikowanych(login,token)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="zmiana roli"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nickUzytkownika: str = str(zapytanie[4])
            nowaRola: str = str(zapytanie[5])
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nickUzytkownika)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
            if(not Hasla.poprawnoscHasla(nowaRola)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.ustawRole(login,token,nickUzytkownika,nowaRola)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="weryfikacja"):
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu)
            
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            login: str = str(zapytanie[2])
            token: str = str(zapytanie[3])
            nickUzytkownika: str = str(zapytanie[4])
            nowaRola: str = str(zapytanie[5])
            kluczePokojuGl: typing.Tuple[str,str] = [str(zapytanie[6]), str(zapytanie[7])]
            
            if((not Nazwy.przetestujNazwe(login)) or (not Kody.przetestujKod(token))):
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(not Nazwy.przetestujNazwe(nickUzytkownika)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
            if(not Hasla.poprawnoscHasla(nowaRola)):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.zweryfikuj(login,token,nickUzytkownika,nowaRola,nazwaProjektu,kluczePokojuGl)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        

        
        else:              #nieznana operacja
            return Pliki.stworzPlikZOdpowiedzia(False,["Nieznana operacja"])
    
    except NameError:
        return Pliki.stworzPlikZOdpowiedzia(False,["Wystąpił nieznany błąd"])
