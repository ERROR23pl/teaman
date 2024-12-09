import ObslugaZapytania as OZ
import sys
import json

if(len(sys.argv)<2):
    print("Nie podano numeru testu!\n")
else:
    nr: int = int(sys.argv[1])
    
    if(nr==0):
        #Test podania nieznanej operacji
        wynik = OZ.ObsluzZapytanie(["nieznane cos","Projekt12345"])
        
    
    elif(nr==1):
        #Test logowania przy niepoprawnej nazwie projektu
        wynik = OZ.ObsluzZapytanie(["logowanie","Proj","Uzytkownik711","Haslo12345"])
        
        
    elif(nr==2):
        #Test logowania przy niepoprawnym loginie
        wynik = OZ.ObsluzZapytanie(["logowanie","Projekt12345","Uz","Haslo12345!"])
    
    elif(nr==3):
        #Test logowania przy niepoprawnym haśle
        wynik = OZ.ObsluzZapytanie(["logowanie","Projekt12345","Uzytkownik711","Has'lo12345!"])
    
    elif(nr==4):
        #Test logowania
        wynik = OZ.ObsluzZapytanie(["logowanie","Projekt12345","Uzytkownik711","Haslo12345!"])
    
    elif(nr==5):
        #Test rejestracji
        wynik = OZ.ObsluzZapytanie(["rejestracja","Projekt12345","1234567890abcde12345AA","Uzytkownik711","Haslo12345!","NickUzytkownika711"])
    
    elif(nr==6):
        #Test tworzenia projektu
        wynik = OZ.ObsluzZapytanie(["tworzenie projektu","Projekt12345","Uzytkownik711","Haslo12345!","NickUzytkownika711"])
    
    elif(nr==7):
        #Test zapraszania do projektu
        wynik = OZ.ObsluzZapytanie(["zapraszanie","Projekt12345","Uzytkownik711","token12345token0987654321A","1234567890abcde12345AA"])
    
    elif(nr==8):
        #Test usuwania projektu
        wynik = OZ.ObsluzZapytanie(["usuwanie projektu","Projekt12345","Uzytkownik711","token12345token0987654321A"])
    
    elif(nr==9):
        #Test tworzenia pokoju
        wynik = OZ.ObsluzZapytanie(["tworzenie pokoju","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788"])
    
    elif(nr==10):
        #Test usuwania pokoju
        wynik = OZ.ObsluzZapytanie(["usuwanie pokoju","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788"])
    
    elif(nr==11):
        #Test dodawania do pokoju
        wynik = OZ.ObsluzZapytanie(["dodawanie do pokoju","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","DodawanyUzytkownik123"])
    
    elif(nr==12):
        #Test usuwania z pokoju
        wynik = OZ.ObsluzZapytanie(["usuwanie z pokoju","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","DodawanyUzytkownik123"])
    
    elif(nr==13):
        #Test pobierania listy pokojów
        wynik = OZ.ObsluzZapytanie(["lista pokojow","Projekt12345","Uzytkownik711","token12345token0987654321A"])
    
    elif(nr==14):
        #Test modyfikacji (dodawanie, usuwanie, modyfikacja) tasków (od razu razem z pobraniem)
        wynik = OZ.ObsluzZapytanie(["modyfikacja taskow","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788",[[1,"nazwaTaska1",[12,2,2025],[100.06,157.0],[2,3,5]],[2,"nazwaTaska2",[1,1,2025],[120.06,17.0],[3]],[3,"nazwaTaska3",[10,1,2025],[20.06,1007.47],[4,5]],[4,"nazwa4",[20,12,2024],[220.06,1004.7],[5]],[5,"nazwaTaska5",[1,12,2024],[426.66,711.711],[]]],[[6,"nazwaTaska6",[11,12,2026],[46.66,71.711],[7]]],[[7,"nazwaTaska7",[1,12,2026],[469.66,71.711],[8]],[8,"nazwaTaska8",[14,7,2026],[568.66,711.711],[1,2,3,4,5]]]])
    
    elif(nr==15):
        #Test zaznaczania tasku jako wykonanego
        wynik = OZ.ObsluzZapytanie(["zaznacz task","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788",1])
    
    elif(nr==16):
        #Test odznaczania tasku jako niewykonanego
        wynik = OZ.ObsluzZapytanie(["odznacz task","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788",1])
    
    elif(nr==17):
        #Test pobierania chatu
        wynik = OZ.ObsluzZapytanie(["pobierz chat","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788"])
    
    elif(nr==18):
        #Test aktualizacji chatu
        wynik = OZ.ObsluzZapytanie(["zaktualizuj chat","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","Uzytkownik711711",1234567788])
    
    elif(nr==19):
        #Test wysyłania wiadomości
        wynik = OZ.ObsluzZapytanie(["wyslij wiadomosc","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","Uzytkownik711711",1234567788,"Wiadomość'admina",123456795])
    
    elif(nr==20):
        #Test pobierania kalendarza
        wynik = OZ.ObsluzZapytanie(["pobierz kalendarz","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788"])
    
    elif(nr==21):
        #Test dodawania wpisu do kalendarza
        wynik = OZ.ObsluzZapytanie(["dodawanie wpisu kalendarza","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","Wpis12345'",[6,7,2025]])
    
    elif(nr==22):
        #Test usuwania wpisu z kalendarza
        wynik = OZ.ObsluzZapytanie(["usuwanie wpisu kalendarza","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","Wpis12345'",[6,7,2025]])
    
    elif(nr==23):
        #Test modyfikowania wpisu kalendarza
        wynik = OZ.ObsluzZapytanie(["modyfikacja wpisu kalendarza","Projekt12345","Uzytkownik711","token12345token0987654321A","Pokoj123456788","Wpis12345'",[6,7,2025],"Wpis711",[7,11,2025]])
    
    
    
    else:
        wynik = "Niepoprawny numer testu\n\n"

    print(wynik)
    dekoder = json.JSONDecoder()
    dane: dict = dekoder.decode(wynik)
    print(dane)