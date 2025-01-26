import rsa

def testPoprawnosciKlucza(klucz:str) -> bool:
    if(klucz.count(".")!=1):
        return False
    
    para = klucz.split(".")
    try:
        n = int(para[0])
        e = int(para[1])
        return True
    except:
        return False

def klucz(klucz: str) -> rsa.PublicKey:
    para = klucz.split(".")
    n = int(para[0])
    e = int(para[1])
    return rsa.PublicKey(n,e)


def generujKluczePokoju():  #[klucz publiczny, klucz prywatny]
    return rsa.newkeys(nbits=2048,poolsize=4)
    


def zaszyfrujKluczPub(kluczUzytkownika: rsa.PublicKey, klucz: rsa.PublicKey) -> str:
    
    n = klucz.n
    e = klucz.e
    
    try:
        return rsa.encrypt(str(n).encode(), kluczUzytkownika).hex()+"."+rsa.encrypt(str(e).encode(), kluczUzytkownika).hex()
    
    except:
        raise NameError("")


def zaszyfrujKluczPriv(kluczUzytkownika: rsa.PublicKey, klucz: rsa.PrivateKey) -> str:
    n = klucz.n
    e = klucz.e
    d = klucz.d
    p = klucz.p
    q = klucz.q
    
    try:
        return rsa.encrypt(str(n).encode(), kluczUzytkownika).hex()+"."+rsa.encrypt(str(e).encode(), kluczUzytkownika).hex()+"."+rsa.encrypt(str(d).encode(), kluczUzytkownika).hex()+"."+rsa.encrypt(str(p).encode(), kluczUzytkownika), rsa.encrypt(str(q).encode(), kluczUzytkownika).hex()

    except:
        raise NameError("")