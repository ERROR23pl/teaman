import typing

def sprawdzAtakSlownikowy(haslo: str) -> bool:      #TODO - DO IMPLEMENTACJI W PRZYSZŁOŚCI; true=nie występuje w słowniku
    return True


def sprawdzCzyMaMalaLitere(haslo: str) -> bool:
    for znak in haslo:
        if(ord(znak) in range (97,123)):
            return True
    
    return False

def sprawdzCzyMaWielkaLitere(haslo: str) -> bool:
    for znak in haslo:
        if(ord(znak) in range (65,91)):
            return True
    
    return False

def sprawdzCzyMaCyfre(haslo: str) -> bool:
    for znak in haslo:
        if(ord(znak) in range (48,58)):
            return True
    
    return False

def sprawdzCzyMaZnakSpecjalny(haslo: str) -> bool:
    for znak in haslo:
        if((ord(znak) in range (33,48)) or (ord(znak) in range (58,65)) or (ord(znak) in range (91,97)) or (ord(znak) in range (123,127))):
            return True
    
    return False


def czyMaCosSpoza(haslo: str) -> bool:
    for znak in haslo:
        if(ord(znak) not in range (33,127)):
            return True
    
    return False


def czyMaWszystkieTypyZnakow(haslo: str) -> bool:
    return (sprawdzCzyMaCyfre(haslo) and sprawdzCzyMaMalaLitere(haslo) and sprawdzCzyMaWielkaLitere(haslo) and sprawdzCzyMaZnakSpecjalny(haslo) and (not czyMaCosSpoza(haslo)))



def czyBrakZabronionychZnakow(haslo: str) -> bool:
    zabronionyZbior: typing.List = [" ",".",",","-","=","/","\\","\'","\""]
    
    for znak in haslo:
        if (znak in zabronionyZbior):
            return False
    
    return True


def testDlugosci(haslo: str) -> bool:
    return len(haslo)>=10


def poprawnoscHasla(haslo: str) -> bool:
    return (testDlugosci(haslo) and czyMaWszystkieTypyZnakow(haslo) and czyBrakZabronionychZnakow(haslo) and sprawdzAtakSlownikowy(haslo))
