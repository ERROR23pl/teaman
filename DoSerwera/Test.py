import ObslugaZapytania as OZ
import sys

if(len(sys.argv)<2):
    print("Nie podano numeru testu!\n")
else:
    nr: int = int(sys.argv[1])
    
    if(nr==1):
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
        wynik = OZ.ObsluzZapytanie(["rejestracja","Projekt12345","1234567890abcde12345AA","Uzytkownik711","Haslo12345!"])
    
    elif(nr==6):
        #Test tworzenia projektu
        wynik = OZ.ObsluzZapytanie(["tworzenie projektu","Projekt12345","Uzytkownik711","Haslo12345!"])
    
    elif(nr==7):
        #Test zapraszania do projektu
        wynik = OZ.ObsluzZapytanie(["zapraszanie","Projekt12345","Uzytkownik711","token12345token0987654321A","1234567890abcde12345AA"])
    
    elif(nr==8):
        #Test usuwania projektu
        wynik = OZ.ObsluzZapytanie(["usuwanie projektu","Projekt12345","Uzytkownik711","token12345token0987654321A"])
    
    print(wynik)