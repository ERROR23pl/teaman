def przetestujNazwe(nazwa: str) -> bool:        #test poprawności loginu lub nazwy projektu itp.
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


def przetestujNazwePliku(nazwa: str) -> bool:        #test poprawności nazwy pliku (dopuszczona kropka, ale max jedna)
    if(len(nazwa)<1):
        return False
    
    licznikKropek: int = 0
    
    for znak in nazwa:
        if(znak=="."):
            licznikKropek+=1
            if(licznikKropek>1):
                return False
        else:
            kodZnaku: int = ord(znak)
            if ((kodZnaku not in range (48,58)) and (kodZnaku not in range (65,91)) and (kodZnaku not in range (97,123)) and znak!="_"):  #nie cyfra, nie wielka lub mała litera i nie _
                return False    #to nie jest poprawna nazwa pliku
    
    return True     #to jest poprawna nazwa pliku


def przetestujHash(nazwa: str) -> bool:
    if(len(nazwa)!=128):
        return False
    
    for znak in nazwa:
        kodZnaku: int = ord(znak)
        if ((kodZnaku not in range (48,58)) and (kodZnaku not in range (65,91)) and (kodZnaku not in range (97,123))):  #nie cyfra, nie wielka lub mała litera
            return False 
    
    return True