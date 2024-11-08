import typing

def czyMaCosSpoza(haslo: str) -> bool:
    for znak in haslo:
        if(ord(znak) not in range (33,127)):
            return True
    
    return False



def czyBrakZabronionychZnakow(haslo: str) -> bool:
    zabronionyZbior: typing.List = [" ",".",",","-","=","/","\\","\'","\""]
    
    for znak in haslo:
        if (znak in zabronionyZbior):
            return False
    
    return True



def poprawnoscHasla(haslo: str) -> bool:                    #test poprawności hasła (pod względem bezpieczeństwa bazy danych)
    return (czyBrakZabronionychZnakow(haslo) and (not czyMaCosSpoza(haslo)))
