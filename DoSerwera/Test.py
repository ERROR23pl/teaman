import ObslugaZapytania as OZ
import sys
import json

if(len(sys.argv)<2):
    print("Nie podano numeru testu!\n")
else:
    nr: int = int(sys.argv[1])
    koder = json.JSONEncoder(ensure_ascii=False)
    slownik: dict = {}
    
    if(nr==0):
        #Test podania nieznanej operacji
        slownik['operacja'] = "nieznane cos"
        slownik['projekt'] = "Projekt12345"
        
    
    elif(nr==1):
        #Test logowania przy niepoprawnej nazwie projektu
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Proj"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Haslo12345"
        
    elif(nr==2):
        #Test logowania przy niepoprawnym loginie
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uz"
        slownik['dana2'] = "Haslo12345!"
    
    elif(nr==3):
        #Test logowania przy niepoprawnym haśle
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Has'lo12345!"
    
    elif(nr==4):
        #Test logowania
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Haslo12345!"
    
    elif(nr==5):
        #Test rejestracji
        slownik['operacja'] = "rejestracja"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "1234567890abcde12345AA"
        slownik['dana2'] = "Uzytkownik711"
        slownik['dana3'] = "Haslo12345!"
        slownik['dana4'] = "NickUzytkownika711"
    
    elif(nr==6):
        #Test tworzenia projektu
        slownik['operacja'] = "tworzenie projektu"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Haslo12345!"
        slownik['dana3'] = "NickUzytkownika711"
    
    elif(nr==7):
        #Test zapraszania do projektu
        slownik['operacja'] = "zapraszanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "1234567890abcde12345AA"
    
    elif(nr==8):
        #Test usuwania projektu
        slownik['operacja'] = "usuwanie projektu"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
    
    elif(nr==9):
        #Test tworzenia pokoju
        slownik['operacja'] = "tworzenie pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==10):
        #Test usuwania pokoju
        slownik['operacja'] = "usuwanie pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==11):
        #Test dodawania do pokoju
        slownik['operacja'] = "dodawanie do pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "DodawanyUzytkownik123"
        slownik['dana5'] = "klucz123"
        slownik['dana6'] = "klucz321"
    
    elif(nr==12):
        #Test usuwania z pokoju
        slownik['operacja'] = "usuwanie z pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "UsuwanyUzytkownik123"
    
    elif(nr==13):
        #Test pobierania listy pokojów
        slownik['operacja'] = "lista pokojow"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
    
    elif(nr==14):
        #Test modyfikacji (dodawanie, usuwanie, modyfikacja) tasków (od razu razem z pobraniem)
        slownik['operacja'] = "modyfikacja taskow"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['DodawanyTask1'] = [1,"nazwaTaska1",[12,2,2025],[100.06,157.0],[2,3,5]]
        slownik['DodawanyTask2'] = [2,"nazwaTaska2",[1,1,2025],[120.06,17.0],[3]]
        slownik['DodawanyTask3'] = [3,"nazwaTaska3",[10,1,2025],[20.06,1007.47],[4,5]]
        slownik['DodawanyTask4'] = [4,"nazwa4",[20,12,2024],[220.06,1004.7],[5]]
        slownik['DodawanyTask5'] = [5,"nazwaTaska5",[1,12,2024],[426.66,711.711],[]]
        slownik['UsuwanyTask1'] = [6,"nazwaTaska6",[11,12,2026],[46.66,71.711],[7]]
        slownik['ModyfikowanyTask1'] = [7,"nazwaTaska7",[1,12,2026],[469.66,71.711],[8]]
        slownik['ModyfikowanyTask2'] = [8,"nazwaTaska8",[14,7,2026],[568.66,711.711],[1,2,3,4,5]]
    
    elif(nr==15):
        #Test zaznaczania tasku jako wykonanego
        slownik['operacja'] = "zaznacz task"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = 1
    
    elif(nr==16):
        #Test odznaczania tasku jako niewykonanego
        slownik['operacja'] = "odznacz task"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = 1
    
    elif(nr==17):
        #Test pobierania chatu
        slownik['operacja'] = "pobierz chat"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==18):
        #Test aktualizacji chatu
        slownik['operacja'] = "zaktualizuj chat"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Uzytkownik711711"
        slownik['dana5'] = 1234567788
    
    elif(nr==19):
        #Test wysyłania wiadomości
        slownik['operacja'] = "wyslij wiadomosc"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Uzytkownik711711"
        slownik['dana5'] = 1234567788
        slownik['dana6'] = "Wiadomość'admina"
        slownik['dana7'] = 123456795
    
    elif(nr==20):
        #Test pobierania kalendarza
        slownik['operacja'] = "pobierz kalendarz"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==21):
        #Test dodawania wpisu do kalendarza
        slownik['operacja'] = "dodawanie wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
    
    elif(nr==22):
        #Test usuwania wpisu z kalendarza
        slownik['operacja'] = "usuwanie wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
    
    elif(nr==23):
        #Test modyfikowania wpisu kalendarza
        slownik['operacja'] = "modyfikacja wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
        slownik['dana6'] = "Wpis711"
        slownik['dana7'] = [7,11,2025]
    
    
    
    else:
        slownik['operacja'] = "Nieznany numer testu"

    wynik = OZ.ObsluzZapytanie(koder.encode(slownik))
    print(wynik)
    dekoder = json.JSONDecoder()
    dane: dict = dekoder.decode(wynik)
    print(dane)
    