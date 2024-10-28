import ManagerKodow as Kody

print("Test generatora:\n")
for n in range(40):
    kod: str = Kody.wygenerujKod()
    if(Kody.przetestujKod(kod)):
        print(kod)
    else:
        print("Wygenerowano niepoprawny kod - "+kod)
    

print("\n\nTest sprawdzania poprawności:\n")

print("Podaj kod do sprawdzenia: ",end="")
kod: str = input()
while (kod!="\0"):
    if(Kody.przetestujKod(kod)):
        print("Kod poprawny")
    else:
        print("Kod niepoprawny")
    print("")