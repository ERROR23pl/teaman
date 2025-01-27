import rsa
import sys

if(len(sys.argv)!=3):
    print("Podano złą ilość argumentów")
else:
    plikNaKluczPub = open(sys.argv[1],"w")
    plikNaKluczPriv = open(sys.argv[2],"w")
    
    (klPub, klPriv) = rsa.newkeys(nbits=6144,poolsize=4)
    
    plikNaKluczPub.write(str(klPub.n)+"."+str(klPub.e))
    plikNaKluczPub.close()
    
    plikNaKluczPriv.write(str(klPriv.n)+"."+str(klPriv.e)+"."+str(klPriv.d)+"."+str(klPriv.p)+"."+str(klPriv.q))
    plikNaKluczPriv.close()