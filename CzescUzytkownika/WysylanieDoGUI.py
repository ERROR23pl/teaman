def wyslijBladDoGUI(GUI, blad: NameError):
    kodBledu: str = str(blad)
    komunikat: str
    
    if(kodBledu=="PustePole"):
        komunikat="Żadne pole nie może być puste!"
    elif(kodBledu=="ZlaNazwaProjektu"):
        komunikat="Podana nazwa projektu nie jest poprawna - nazwa musi mieć minimum dziesięć znaków i może składać się tylko z liter, cyfr oraz znaku '_'!"
    elif(kodBledu=="ZlyLogin"):
        komunikat="Podany login nie jest poprawny - login musi mieć minimum dziesięć znaków i może składać się tylko z liter, cyfr oraz znaku '_'!"
    elif(kodBledu=="ZlyZnakWHasle"):
        komunikat="Podane hasło zawiera niedozwolony znak!"
    elif(kodBledu=="BladPolZSerwerem"):
        komunikat="Wystąpił błąd połączenia z serwerem!"
    elif(kodBledu=="ProjNieIstnieje"):
        komunikat="Projekt o podanej nazwie nie istnieje!"
    elif(kodBledu=="NieudaneLogowanie"):
        komunikat="Logowanie nie powiodło się"
    elif(kodBledu=="ZlyKod"):
        komunikat="Podany kod nie jest poprawny - kod musi mieć od dwudziestu do trzydziestu znaków i może składać się tylko z liter i cyfr!"
    elif(kodBledu=="ZleHaslo"):
        komunikat="Podane hasło nie spełnia założeń - hasło musi mieć minimum dziesięć znaków, w tym minimum jedną małą literę, jedną wielką literę, jedną cyfrę i jeden dozwolony znak specjalny!"
    elif(kodBledu=="KodNieIstnieje"):
        komunikat="Podany kod nie istnieje! Być może już wygasł lub został wykorzystany."
    elif(kodBledu=="LoginIstnieje"):
        komunikat="Podany login już istnieje w wybranym projekcie!"
    elif(kodBledu=="ProjIstnieje"):
        komunikat="Projekt o podanej nazwie już istnieje!"
    elif(kodBledu=="NiepolZProj"):
        komunikat="Nie jesteś połączony z żadnym projektem!"
    elif(kodBledu=="BrakTokenu"):
        komunikat="Nie jesteś zalogowany!"
    elif(kodBledu=="ZlyToken"):
        komunikat="Wystąpił błąd sesji - zaloguj się jeszcze raz!"
    elif(kodBledu=="TokenNiepopr"):
        komunikat="Sesja wygasła lub nie posiadasz wymaganych uprawnień do tej operacji!"
    
    else:
        komunikat="Wystąpił nieznany błąd!"
    
    GUI.wyswietlBlad(komunikat)