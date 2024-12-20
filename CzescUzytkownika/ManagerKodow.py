import random

def wygenerujKod() -> str:
    kod: str = ""
    dl: int = random.randint(20,30)
    for i in range(dl):
        typZnaku: int = random.randint(1,3)
        if(typZnaku==1):
            kod=kod+chr(random.randint(48,57))    #losowa cyfra
        elif(typZnaku==2):
            kod=kod+chr(random.randint(65,90))    #losowa wielka litera
        else:
            kod=kod+chr(random.randint(97,122))    #losowa mała litera
    
    return kod


def przetestujKod(kod: str) -> bool:
    if(len(kod) not in range(20,31)):
        return False
    
    for znak in kod:
        kodZnaku: int = ord(znak)
        if ((kodZnaku not in range (48,58)) and (kodZnaku not in range (65,91)) and (kodZnaku not in range (97,123))):  #nie cyfra i nie wielka lub mała litera
            return False    #to nie jest poprawny kod
    
    return True     #to jest poprawny kod