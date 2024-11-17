def przetestujNazwe(nazwa: str) -> bool:        #test poprawności loginu lub nazwy projektu
    if(len(nazwa)<10):
        return False
    
    for znak in nazwa:
        kodZnaku: int = ord(znak)
        if ((kodZnaku not in range (48,58)) and (kodZnaku not in range (65,91)) and (kodZnaku not in range (97,123)) and znak!="_"):  #nie cyfra, nie wielka lub mała litera i nie _
            return False    #to nie jest poprawny kod
    
    return True     #to jest poprawny kod


def zabezpieczCudzyslowy(tekst: str) -> str:
    wynik=""
    for znak in tekst:
        if(znak=="'" or znak=="\""):
            wynik = wynik+"\\"+znak
        else:
            wynik+=znak
    return wynik