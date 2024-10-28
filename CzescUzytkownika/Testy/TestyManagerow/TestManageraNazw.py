import ManagerNazw as Nazwy

print("Test sprawdzania poprawności:\n")

print("Podaj nazwę do sprawdzenia: ",end="")
nazwa: str = input()
while (nazwa!="\0"):
    if(Nazwy.przetestujNazwe(nazwa)):
        print("Nazwa poprawna")
    else:
        print("Nazwa niepoprawna")
    print("")