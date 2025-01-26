import sys
import json
import hashlib as hash
import requests
import rsa

klPub = rsa.PublicKey(17816310546552771655439713107616840115562925053438091325857197620543869325897175840981130276572067437736315733822297846008390603764583101370018840858983612018207395260107083971809314588848158184203986312247831637935725701847240175846019660565277392151165184199105353864616026039404903193819542740959993827594505304539132751777030472435146595147977089132536497774490099341340658336986419432321325827653454938594105158008702361354419168022899006965743065402285381849835285246080479200499102949036438636723615651366520528794838732460618399146551091817246072785687544394284413744051945209665803099454047736976345547563349344123651404038128571196484154546434343059421454481211114972989370009393957678142507246295935206452702931063245156389312692299388108069036166681146470956049997998067999104775783487944529694506731103437845793098754626326809284946911371325474715608706840126992722051789463988998041227681512932678573796280898278381837083663444778558710472939280595381824969353949984887482747948263087676994683158620036255408822846015852001042788017591085597553151286821165434553060002705963480896635685821083864329911822195119930099186736223473427898336268921289614747062520293754339846548508958257459098107931430760009549784050693116794935680488833565403459015597014065575999247407152372845478233430937770788078006557140484775148167177806033373901193310473118078134279860910509005628281298360018902188606004239245730062377849144472659583044820401943131511465789344597380685946566655058839807777566197844919051217625132384054669558157220061904886966920609990149714263512386063969356809600185549654231123434266099271906884841318198234704955139545814465393684645570090197198283841536989135080744628034992935015719438129839900038655132513882838751627512415878806910769466662865796160592274775384715047584116972488132452702384387747877650891063602865389893,65537)
klPriv = rsa.PrivateKey(17816310546552771655439713107616840115562925053438091325857197620543869325897175840981130276572067437736315733822297846008390603764583101370018840858983612018207395260107083971809314588848158184203986312247831637935725701847240175846019660565277392151165184199105353864616026039404903193819542740959993827594505304539132751777030472435146595147977089132536497774490099341340658336986419432321325827653454938594105158008702361354419168022899006965743065402285381849835285246080479200499102949036438636723615651366520528794838732460618399146551091817246072785687544394284413744051945209665803099454047736976345547563349344123651404038128571196484154546434343059421454481211114972989370009393957678142507246295935206452702931063245156389312692299388108069036166681146470956049997998067999104775783487944529694506731103437845793098754626326809284946911371325474715608706840126992722051789463988998041227681512932678573796280898278381837083663444778558710472939280595381824969353949984887482747948263087676994683158620036255408822846015852001042788017591085597553151286821165434553060002705963480896635685821083864329911822195119930099186736223473427898336268921289614747062520293754339846548508958257459098107931430760009549784050693116794935680488833565403459015597014065575999247407152372845478233430937770788078006557140484775148167177806033373901193310473118078134279860910509005628281298360018902188606004239245730062377849144472659583044820401943131511465789344597380685946566655058839807777566197844919051217625132384054669558157220061904886966920609990149714263512386063969356809600185549654231123434266099271906884841318198234704955139545814465393684645570090197198283841536989135080744628034992935015719438129839900038655132513882838751627512415878806910769466662865796160592274775384715047584116972488132452702384387747877650891063602865389893,65537,3468005457106271388810052643756473890386136608430500801744972611582436501372816457930577825323555614434627459547599884363474662133219198684366546421686283145647065647392863118976630395195629246927540982732587518579520771144013960408130869735130440692622705568274211502676452144356445214818437016439974995172545343393895303636412678896732610804625535591555428263563638819254509336785872906878910441176360294972992347844988571704507763957277913726017124453926096956808348473141106140970246674715929134514597324633149249825835142133452994764980885275685615004150571491491619484152015884762907214851691212301558511226721509727107144991598733276676508835449637829150548466008669815683131562473697576942245829699211825819264404711442672994773364903234723814588619838433030654230889794487899424441531805784646311439680923547867598189737289898089721044108646474496558387174769205169115320126119458013640036410209681204100251444036436718695047429570593996887935280919799376885957492024907407576471837067525111164721087776200400899476544619506688995437708826044468650742427833576219857581996033895832579305713918748196222575314210621525596302479747984885638060466393426931177459320716892397179507227780795323678789588073952460488919350572358717085168931641565888724364510997251796721558806932205320884360327035914527104076569519703369901306006711620073147269427497831875356602945174511885992229947754278906167803858728695514125041088090554050352264336511637109816994727228642004877112069530688717376372616259987548675185882858099112869708520674461420908842156710029563224927082607951321771476183909157478392592972685583006907926860775254916315255749012514575049421158270324049707334820726446885918203351485110897297251966614481901411247202871692038633502536085273450629972169016592079987987932373445006998932817916170784082935894511160442152900199352737800381,24308291749194918295930689667231740781422364776024164584415151209402908426512604799317142020981698123864379830963426348528242742239929364314566093920784532015411849063836343101092019699646571643208261733241319956554566912251241626675678483876943632330968145471355118802925290843539172676030102700616664619988741677889031709889227516608015861229950904507420014410356709399512453994125351011213423682049424714321385227151652461461972009991585908335995376647808893211252948534205524713939117681826904584415453168775480272503705255773599868078811721604610815680216326937405446898360845778487131851946346753333724366109818562581529400588789442400809977745449479404687433766947949741944885434926379971841617714787350905346053851215968395857171772817229922164153333324815250587717262916123336291374075879965136095033840423556274122293716215800595273828337179514536297762638337007145002803687965698391708643972053264641491525338706222415712859597657535096058529270435434910862281367984346219,732931410005100063190270926179102405598999618479039487370063885410495746234019915752417634888167234760244991530845133596938739770153570758094398933385514606978896183137192795081184838467861751827976376787380940160840982148726655882993647654662726228515291540279646737720447435554438319278843066687448781582230667927301791088755869030321272119251593711025136956739527386568620572367448269953539534665311131726788160060137040462209560176590170010638408707632583641539363992713380967780213177158023949430410431913121960015421972532190393029929960952300670157292755526979573808969627030641800123073343896354607873416068442898779630437083505459120102591630199042332034682496844988233080872050461744441164656769992010082693974102972682300828420872043978435388965891812785280349721050495639588171225085553275582444313460509645101405444386245664431577403359718335814846770447)

if(len(sys.argv)<2):
    print("Nie podano numeru testu!\n")
else:
    nr: int = int(sys.argv[1])
    koder = json.JSONEncoder(ensure_ascii=False)
    slownik: dict = {}
    
    if(nr==0):
        #Test podania nieznanej operacji
        slownik['operacja'] = "nieznane cos"
        slownik['projekt'] = "Projekt12345"
        
    
    elif(nr==1):
        #Test logowania przy niepoprawnej nazwie projektu
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Proj"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Haslo12345"
        
    elif(nr==2):
        #Test logowania przy niepoprawnym loginie
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uz"
        slownik['dana2'] = "Haslo12345!"
    
    elif(nr==3):
        #Test logowania przy niepoprawnym haśle
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Has'lo12345!"
    
    elif(nr==4):
        #Test logowania
        slownik['operacja'] = "logowanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "Haslo12345!"
    
    elif(nr==5):
        #Test rejestracji
        slownik['operacja'] = "rejestracja"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "1234567890abcde12345AA"
        slownik['dana2'] = hash.sha3_512(("Uzytkownik711").encode()).hexdigest()
        slownik['dana3'] = hash.sha3_512(("Haslo12345!").encode()).hexdigest()
        slownik['dana4'] = "NickUzytkownika711"
    
    elif(nr==6):
        #Test tworzenia projektu
        slownik['operacja'] = "tworzenie projektu"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = hash.sha3_512(("Uzytkownik711").encode()).hexdigest()
        slownik['dana2'] = hash.sha3_512(("Haslo12345!").encode()).hexdigest()
        slownik['dana3'] = "NickUzytkownika711"
        slownik['dana4'] = str(klPub.n)+"."+str(klPub.e)
    
    elif(nr==7):
        #Test zapraszania do projektu
        slownik['operacja'] = "zapraszanie"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = hash.sha3_512(("1234567890abcde12345AA").encode()).hexdigest()
    
    elif(nr==8):
        #Test usuwania projektu
        slownik['operacja'] = "usuwanie projektu"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
    
    elif(nr==9):
        #Test tworzenia pokoju
        slownik['operacja'] = "tworzenie pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==10):
        #Test usuwania pokoju
        slownik['operacja'] = "usuwanie pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==11):
        #Test dodawania do pokoju
        slownik['operacja'] = "dodawanie do pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "DodawanyUzytkownik123"
        slownik['dana5'] = "klucz123"
        slownik['dana6'] = "klucz321"
    
    elif(nr==12):
        #Test usuwania z pokoju
        slownik['operacja'] = "usuwanie z pokoju"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "UsuwanyUzytkownik123"
    
    elif(nr==13):
        #Test pobierania listy pokojów
        slownik['operacja'] = "lista pokojow"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
    
    elif(nr==14):
        #Test modyfikacji (dodawanie, usuwanie, modyfikacja) tasków (od razu razem z pobraniem)
        slownik['operacja'] = "modyfikacja taskow"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['DodawanyTask1'] = [1,"nazwaTaska1",[12,2,2025],[100.06,157.0],[2,3,5]]
        slownik['DodawanyTask2'] = [2,"nazwaTaska2",[1,1,2025],[120.06,17.0],[3]]
        slownik['DodawanyTask3'] = [3,"nazwaTaska3",[10,1,2025],[20.06,1007.47],[4,5]]
        slownik['DodawanyTask4'] = [4,"nazwaTaska4",[20,12,2024],[220.06,1004.7],[5]]
        slownik['DodawanyTask5'] = [5,"nazwaTaska5",[1,12,2024],[426.66,711.711],[1]]
        slownik['DodawanyTask6'] = [6,"nazwaTaska6",[11,12,2026],[46.66,71.711],[7,8]]
        slownik['DodawanyTask7'] = [7,"nazwaTaska7",[1,12,2026],[469.66,71.711],[1]]
        slownik['DodawanyTask8'] = [8,"nazwaTaska8",[14,7,2026],[568.66,711.711],[1]]
        slownik['UsuwanyTask1'] = [5,"nazwaTaska5",[11,12,2026],[46.66,71.711],[1]]
        slownik['ModyfikowanyTask1'] = [7,"nazwaTaska71",[1,12,2026],[469.66,71.711],[8]]
        slownik['ModyfikowanyTask2'] = [8,"nazwaTaska81",[14,7,2026],[568.66,711.711],[1,2,3,4,5]]
    
    elif(nr==15):
        #Test zaznaczania tasku jako wykonanego
        slownik['operacja'] = "zaznacz task"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = 1
    
    elif(nr==16):
        #Test odznaczania tasku jako niewykonanego
        slownik['operacja'] = "odznacz task"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = 1
    
    elif(nr==17):
        #Test pobierania chatu
        slownik['operacja'] = "pobierz chat"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==18):
        #Test aktualizacji chatu
        slownik['operacja'] = "zaktualizuj chat"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Uzytkownik711711"
        slownik['dana5'] = 1234567788
    
    elif(nr==19):
        #Test wysyłania wiadomości
        slownik['operacja'] = "wyslij wiadomosc"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Uzytkownik711711"
        slownik['dana5'] = 1234567788
        slownik['dana6'] = "Wiadomość'admina"
    
    elif(nr==20):
        #Test pobierania kalendarza
        slownik['operacja'] = "pobierz kalendarz"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
    
    elif(nr==21):
        #Test dodawania wpisu do kalendarza
        slownik['operacja'] = "dodawanie wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
    
    elif(nr==22):
        #Test usuwania wpisu z kalendarza
        slownik['operacja'] = "usuwanie wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
    
    elif(nr==23):
        #Test modyfikowania wpisu kalendarza
        slownik['operacja'] = "modyfikacja wpisu kalendarza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Wpis12345"
        slownik['dana5'] = [6,7,2025]
        slownik['dana6'] = "Wpis711"
        slownik['dana7'] = [7,11,2025]
    
    elif(nr==24):
        #Test dodawania pliku
        slownik['operacja'] = "dodawanie pliku"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Plik711.uwu"
        slownik['dana5'] = "Zdecydowanie bardzo ważna zawartość pliku\nUwU"
    
    elif(nr==25):
        #Test usuwania pliku
        slownik['operacja'] = "usuwanie pliku"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Plik711.uwu"
    
    elif(nr==26):
        #Test pobierania pliku
        slownik['operacja'] = "pobranie pliku"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"
        slownik['dana4'] = "Plik711.uwu"
    
    elif(nr==27):
        #Test pobierania listy plików z pokoju
        slownik['operacja'] = "pobranie listy plikow"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "Pokoj123456788"

    elif(nr==28):
        #Test ustawiania klucza użytkownika
        slownik['operacja'] = "ustawianie klucza"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "klucz1234567890"
    
    elif(nr==29):
        #Test pobierania klucza publicznego użytkownika
        slownik['operacja'] = "pobieranie klucza uzytkownika"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "NickInnegoUzytkownika12711"
    
    elif(nr==30):
        #Test pobierania listy niezweryfikowanych użytkowników
        slownik['operacja'] = "lista niezweryfikowanych"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token

    elif(nr==31):
        #Test ustawiania użytkownikowi nowej roli
        slownik['operacja'] = "zmiana roli"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "NickInnegoUzytkownika12711"
        slownik['dana4'] = "NowaRola123456788"
    
    elif(nr==32):
        #Test weryfikacji użytkownika
        slownik['operacja'] = "weryfikacja"
        slownik['projekt'] = "Projekt12345"
        slownik['dana1'] = "Uzytkownik711"
        slownik['dana2'] = "token12345token0987654321A"     # tu zwrócony w terminalu token
        slownik['dana3'] = "NickInnegoUzytkownika12711"
        slownik['dana4'] = "NowaRola123456788"
        slownik['dana5'] = "ZdecydowanieZaszyfrowanyKluczPubliczny"
        slownik['dana6'] = "ZdecydowanieZaszyfrowanyKluczPrywatny"
    
    
    else:
        slownik['operacja'] = "Nieznany numer testu"

    wynik = requests.post("http://localhost:8000",json=koder.encode(slownik))
    dekoder = json.JSONDecoder()
    dane: dict = dekoder.decode(wynik.text)
    print(dane)
    