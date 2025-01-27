import ManagerPlikowKomunikacyjnych as Pliki
import KomunikacjaZBaza as Bazy
import Obiekty as o
import typing
import ObslugaKont as ObKont
import ObslugaPokojow as ObPokojow
import ObslugaTaskow as ObTask
import ObslugaChatow as ObChatow
import ObslugaKalendarza as ObKal
import ObslugaPlikow as ObPlikow
import ObslugaKluczyIWeryfikacji as ObWer



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
            return ObKont.obsluzLogowanie(zapytanie,nazwaProjektu,czyProjektIstnieje)

        
        elif(operacja=="rejestracja"):
            return ObKont.obsluzRejestracje(zapytanie,nazwaProjektu,czyProjektIstnieje)

        
        elif(operacja=="tworzenie projektu"):
            return ObKont.obsluzTworzenieProjektu(zapytanie,nazwaProjektu,czyProjektIstnieje)

        
        elif(operacja=="zapraszanie"):
            return ObKont.obsluzZapraszanie(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="usuwanie projektu"):
            return ObKont.obsluzUsuwanieProjektu(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="tworzenie pokoju"):
            return ObPokojow.obsluzTworzeniePokoju(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="usuwanie pokoju"):
            return ObPokojow.obsluzUsuwaniePokoju(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="dodawanie do pokoju"):
            return ObPokojow.obsluzDodawanieDoPokoju(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="usuwanie z pokoju"):
            return ObPokojow.obsluzUsuwanieZPokoju(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="lista pokojow"):
            return ObPokojow.obsluzPobieranieListyPokojow(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        
        elif(operacja=="modyfikacja taskow"):
            return ObTask.obsluzModTaskow(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        
        elif(operacja=="pobierz taski"):
            return ObTask.obsluzPobranieListyTaskow(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        
        elif(operacja=="zaznacz task"):
            return ObTask.obsluzZaznaczenieTaska(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        
        elif(operacja=="odznacz task"):
            return ObTask.obsluzOdznaczenieTaska(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="pobierz chat"):
            return ObChatow.obsluzPobranieChatu(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="zaktualizuj chat"):
            return ObChatow.obsluzAktChatu(zapytanie,nazwaProjektu,czyProjektIstnieje)

        
        
        elif(operacja=="wyslij wiadomosc"):
            return ObChatow.obsluzWyslanieWiadomosci(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="pobierz kalendarz"):
            return ObKal.obsluzPobranieKalendarza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="dodawanie wpisu kalendarza"):
            return ObKal.obsluzDodawanieDoKalendarza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="usuwanie wpisu kalendarza"):
            return ObKal.obsluzUsuwanieZKalendarza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="modyfikacja wpisu kalendarza"):
            return ObKal.obsluzModWpisuKalendarza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="dodawanie pliku"):
            return ObPlikow.obsluzDodawaniePliku(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="usuwanie pliku"):
            return ObPlikow.obsluzUsuwaniePliku(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="pobranie pliku"):
            return ObPlikow.obsluzPobraniePliku(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="pobranie listy plikow"):
            return ObPlikow.obsluzPobranieListyPlikow(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="ustawianie klucza"):
            return ObWer.obsluzUstawianieKlucza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="pobieranie klucza uzytkownika"):
            return ObWer.obsluzPobieranieCzyjegosKlucza(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="lista niezweryfikowanych"):
            return ObWer.obsluzPobieranieListyNiezweryfikowanych(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="zmiana roli"):
            return ObWer.obsluzZmianeRoli(zapytanie,nazwaProjektu,czyProjektIstnieje)
        
        
        elif(operacja=="weryfikacja"):
            return ObWer.obsluzWeryfikacje(zapytanie,nazwaProjektu,czyProjektIstnieje)
        

        
        else:              #nieznana operacja
            return Pliki.stworzPlikZOdpowiedzia(False,["Nieznana operacja"])
    
    except NameError:
        return Pliki.stworzPlikZOdpowiedzia(False,["Wystąpił nieznany błąd"])
