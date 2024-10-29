import ManagerHasel as Hasla

print("Test sprawdzania poprawności:\n")

print("Podaj hasło do sprawdzenia: ",end="")
haslo: str = input()
while (haslo!="\0"):
    if(Hasla.poprawnoscHasla(haslo)):
        print("Hasło poprawne")
    else:
        print("Hasło niepoprawne - łamie następujące reguły:")
        if(not Hasla.sprawdzAtakSlownikowy(haslo)):
            print("-nieodporne na atak słownikowy")
        if(not Hasla.sprawdzCzyMaMalaLitere(haslo)):
            print("-nie ma małej litery")
        if(not Hasla.sprawdzCzyMaWielkaLitere(haslo)):
            print("-nie ma wielkiej litery")
        if(not Hasla.sprawdzCzyMaCyfre(haslo)):
            print("-nie ma cyfry")
        if(not Hasla.sprawdzCzyMaZnakSpecjalny(haslo)):
            print("-nie ma znaku specjalnego")
        if(Hasla.czyMaCosSpoza(haslo)):
            print("-posiada niestandardowy znak")
        if(not Hasla.czyBrakZabronionychZnakow(haslo)):
            print("-posiada niedozwolony znak")
        if(not Hasla.testDlugosci(haslo)):
            print("-nie ma minimum dziesięciu znaków")
        
    print("\nPodaj hasło do sprawdzenia: ",end="")
    haslo: str = input()
        