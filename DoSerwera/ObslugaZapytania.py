import ManagerPlikowKomunikacyjnych as Pliki
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
import Obiekty as o
import typing
import hashlib as hash


#TODO plik w rozwoju; po zakończeniu, przerzucić case'y do osobnych plików, a tu tylko wywołania

def ObsluzZapytanie(plikKomunikacyjny):
    try:
        zapytanie: typing.List = Pliki.analizaPliku(plikKomunikacyjny)
        operacja: str = str(zapytanie[0])
        
        try:
            nazwaProjektu: o.nazwa = o.nazwa(str(zapytanie[1]))
            czyProjektIstnieje: bool = Bazy.czyBazaIstnieje(nazwaProjektu.wart)
        except:
            return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa projektu nie spełnia założeń"])   #niepoprawna nazwa projektu
        
        
        if(operacja=="logowanie"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                haslo: o.haslo = o.haslo(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaLogowania(login.wart,haslo.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="rejestracja"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                kodZapr: o.kod = o.kod(str(zapytanie[2]))
                login: o.nazwa = o.nazwa(str(zapytanie[3]))
                haslo: o.haslo = o.haslo(str(zapytanie[4]))
                nick: o.nazwa = o.nazwa(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(login==hash.sha3_512(nick.wart.encode()).hexdigest()):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaRejestracji(nazwaProjektu.wart,kodZapr.wart,login.wart,haslo.wart,nick.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="tworzenie projektu"):
            if(czyProjektIstnieje):
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt istnieje"])   #nie można stworzyć projektu, bo już istnieje
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                haslo: o.haslo = o.haslo(str(zapytanie[3]))
                nick: o.nazwa = o.nazwa(str(zapytanie[4]))
                kluczPub: o.klucz = o.klucz(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            if(login.wart==hash.sha3_512(nick.wart.encode()).hexdigest()):
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick taki jak login"])   #niepoprawne dane - nazwa publiczna nie może być taka jak login
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.stworzProjekt(nazwaProjektu.wart,login.wart,haslo.wart,nick.wart,kluczPub.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        elif(operacja=="zapraszanie"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                kodZapr: o.kod = o.kod(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy kod"])   #niepoprawny kod - prośba o nowy
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.dodajZaproszenie(login.wart,token.wart,kodZapr.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie projektu"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.usunProjekt(nazwaProjektu.wart,login.wart,token.wart)
            
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="tworzenie pokoju"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.stworzPokoj(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie pokoju"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            if(nazwaProjektu.wart==nazwaPokoju.wart):
                return Pliki.stworzPlikZOdpowiedzia(False, dane=["Nie można usunąć pokoju głównego"])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.usunPokoj(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie do pokoju"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                dodawanyUzytkownik: o.nazwa = o.nazwa(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick dodawanego użytkownika
            
            kluczePokojuZaszyfrowaneKluczemDodawanego: typing.Tuple[str,str] = [str(zapytanie[6]),str(zapytanie[7])]
            
            rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.dodajDoPokoju(login.wart,token.wart,nazwaPokoju.wart,dodawanyUzytkownik.wart,kluczePokojuZaszyfrowaneKluczemDodawanego)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie z pokoju"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                usuwanyUzytkownik: o.nazwa = o.nazwa(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick usuwanego użytkownika
            
            rezultat: typing.Tuple[bool,typing.List[str]] = CzlPokojow.usunZPokoju(login.wart,token.wart,nazwaPokoju.wart,usuwanyUzytkownik.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="lista pokojow"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
            rezultat: typing.Tuple[bool,typing.List[str]] = Pokoje.listaPokojow(login.wart,token.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="modyfikacja taskow"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            dodawaneTaski: typing.List[o.Task] = zapytanie[5]
            usuwaneTaski: typing.List[o.Task] = zapytanie[6]
            modyfikowaneTaski: typing.List[o.Task] = zapytanie[7]                    
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.obslugaTaskow(login.wart,token.wart,nazwaPokoju.wart,dodawaneTaski,usuwaneTaski,modyfikowaneTaski)
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login.wart,token.wart,nazwaPokoju.wart))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="pobierz taski"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju   
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.pobierzTaski(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="zaznacz task"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            idTaska: int = int(zapytanie[5])   
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoWykonany(login.wart,token.wart,nazwaPokoju.wart,idTaska)
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login.wart,token.wart,nazwaPokoju.wart))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        
        elif(operacja=="odznacz task"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            idTaska: int = int(zapytanie[5])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Taski.oznaczJakoNiewykonany(login.wart,token.wart,nazwaPokoju.wart,idTaska)
            
            Bazy.rozlaczZBaza()
            if(rezultat[0]):
                nowaListaTaskow: typing.List[str] = (Taski.pobierzTaski(login.wart,token.wart,nazwaPokoju.wart))[1]
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],nowaListaTaskow)
            else:
                return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobierz chat"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju 
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.pobierzChat(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="zaktualizuj chat"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                ostatniaPosiadana: o.Wiadomosc = o.Wiadomosc(int(zapytanie[6]),True,autorWiadomosci=str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick autora ostatniej wiadomości
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.zaktualizujChat(login.wart,token.wart,nazwaPokoju.wart,ostatniaPosiadana)
                
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])

        
        
        elif(operacja=="wyslij wiadomosc"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                ostatniaPosiadana: o.Wiadomosc = o.Wiadomosc(int(zapytanie[6]),True,autorWiadomosci=str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick autora ostatniej wiadomości  
            
            wiadomosc: o.Wiadomosc = o.Wiadomosc(int(zapytanie[8]),False,trescWiadomosci=str(zapytanie[7]))
            rezultat: typing.Tuple[bool,typing.List[str]] = Chaty.wyslijWiadomosc(login.wart,token.wart,nazwaPokoju.wart,ostatniaPosiadana,wiadomosc)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobierz kalendarz"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.pobierzKalendarz(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie wpisu kalendarza"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis: o.WpisKalendarza = o.WpisKalendarza(str(zapytanie[5]),zapytanie[6])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.dodajDoKalendarza(login.wart,token.wart,nazwaPokoju.wart,wpis)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie wpisu kalendarza"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis: o.WpisKalendarza = o.WpisKalendarza(str(zapytanie[5]),zapytanie[6])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.usunZKalendarza(login.wart,token.wart,nazwaPokoju.wart,wpis)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="modyfikacja wpisu kalendarza"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            wpis: o.WpisKalendarza = o.WpisKalendarza(str(zapytanie[5]),zapytanie[6])
            noweDane: o.WpisKalendarza = o.WpisKalendarza(str(zapytanie[7]),zapytanie[8])
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Kalendarz.modyfikujWpisKalendarza(login.wart,token.wart,nazwaPokoju.wart,wpis,noweDane)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="dodawanie pliku"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                nazwaPliku: o.nazwaPliku = o.nazwaPliku(str(zapytanie[5]))
                zawartoscPliku: bytes = (str(zapytanie[6])).encode()
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa pliku
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.dodajPlik(login.wart,token.wart,nazwaPokoju.wart,nazwaPliku.wart,zawartoscPliku)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="usuwanie pliku"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                nazwaPliku: o.nazwaPliku = o.nazwaPliku(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa plikuu
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.usunPlik(login.wart,token.wart,nazwaPokoju.wart,nazwaPliku.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobranie pliku"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            try:
                nazwaPliku: o.nazwaPliku = o.nazwaPliku(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pliku nie spełnia założeń"])   #niepoprawna nazwa pliku
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzPlik(login.wart,token.wart,nazwaPokoju.wart,nazwaPliku.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobranie listy plikow"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nazwaPokoju: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nazwa pokoju nie spełnia założeń"])   #niepoprawna nazwa pokoju
            
            rezultat: typing.Tuple[bool,typing.List[str]] = udPlikow.pobierzListePlikow(login.wart,token.wart,nazwaPokoju.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="ustawianie klucza"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                kluczPub: o.klucz = o.klucz(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Wyślij nowy klucz"])   #niepoprawny klucz - prośba o nowy
            
            rezultat: typing.Tuple[bool,typing.List[str]] = LogIRej.probaUstawieniaKluczaPublicznego(login.wart,token.wart,kluczPub.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="pobieranie klucza uzytkownika"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
                nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            rezultat: typing.Tuple[bool,typing.List[str]] = WlProj.pobierzKluczPublicznyUzytkownika(login.wart,token.wart,nickUzytkownika.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="lista niezweryfikowanych"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane

            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.listaNiezweryfikowanych(login.wart,token.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="zmiana roli"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
            try:
                nowaRola: o.nazwa = o.nazwa(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.ustawRole(login.wart,token.wart,nickUzytkownika.wart,nowaRola.wart)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        
        
        elif(operacja=="weryfikacja"):
            if(czyProjektIstnieje):
                Bazy.polaczZBaza(nazwaProjektu.wart)
            else:
                return Pliki.stworzPlikZOdpowiedzia(False,["Projekt nie istnieje"])   #niepoprawna nazwa projektu
            
            try:
                login: o.nazwa = o.nazwa(str(zapytanie[2]))
                token: o.kod = o.kod(str(zapytanie[3]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Dane nie spełniają założeń"])   #niepoprawne dane
            
            try:
                nickUzytkownika: o.nazwa = o.nazwa(str(zapytanie[4]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nick drugiego użytkownika nie spełnia założeń"])   #niepoprawny nick celu
            
            try:
                nowaRola: o.nazwa = o.nazwa(str(zapytanie[5]))
            
            except:
                return Pliki.stworzPlikZOdpowiedzia(False,["Nowa rola nie spełnia założeń"])   #niepoprawna rola
            
            kluczePokojuGl: typing.Tuple[str,str] = [str(zapytanie[6]), str(zapytanie[7])]
            
            rezultat: typing.Tuple[bool,typing.List[str]] = Wer.zweryfikuj(login.wart,token.wart,nickUzytkownika.wart,nowaRola.wart,nazwaProjektu.wart,kluczePokojuGl)
            
            Bazy.rozlaczZBaza()
            return Pliki.stworzPlikZOdpowiedzia(rezultat[0],rezultat[1])
        

        
        else:              #nieznana operacja
            return Pliki.stworzPlikZOdpowiedzia(False,["Nieznana operacja"])
    
    except NameError:
        return Pliki.stworzPlikZOdpowiedzia(False,["Wystąpił nieznany błąd"])
