-- notes:
-- * some of these varchars may have to change to TEXT datatype
-- * if varchar is used, maybe try to make some kind of wrapper around the string to make sure no bugs can crawl up

CREATE TABLE Role (
    nazwa VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Uzytkownicy (
    nazwa VARCHAR(255) PRIMARY KEY,
    login VARCHAR(64) NOT NULL, -- sha256 produces a 64 character long hash
    haslo VARCHAR(64) NOT NULL, -- sha256 produces a 64 character long hash
    token VARCHAR(255),
    rola VARCHAR(255) NOT NULL,
    last_update DATE,

    -- todo: jak długie jest szyfrowanie?
    -- ! klucz publiczny jest null tylko i wyłącznie pomiędzy stworzeniem użytkowanika a zaakceptowaniem klucza przez serwer (unique)
    klucz_publiczny VARCHAR(64) UNIQUE,

    CONSTRAINT rola FOREIGN KEY (rola) REFERENCES Role(nazwa)
);

CREATE TABLE KodyZaproszeniowe (
    kod VARCHAR(255) PRIMARY KEY, -- todo: jak długie są kody zaproszeniowe?
    data_dodania DATE NOT NULL
);

CREATE TABLE Pokoje (
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE CzlonkowiePokojow (
    id INTEGER PRIMARY KEY,
    uzytkownik VARCHAR(255) NOT NULL,
    pokoj INTEGER NOT NULL,

    CONSTRAINT uzytkownik FOREIGN KEY (uzytkownik) REFERENCES Uzytkownicy(nazwa),
    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(id)
);

CREATE TABLE Wiadomosci (
    id INTEGER PRIMARY KEY,
    pokoj INTEGER NOT NULL,
    tresc TEXT NOT NULL,
    data_wyslania DATE NOT NULL,
    autor VARCHAR(255) NOT NULL,

    CONSTRAINT autor FOREIGN KEY (autor) REFERENCES Uzytkownicy(nazwa),
    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(id)
);

CREATE TABLE Wydarzenia (
    id INTEGER PRIMARY KEY,
    pokoj INTEGER NOT NULL,
    nazwa_wydarzenia VARCHAR(255) NOT NULL,
    data_wydarzenia DATE NOT NULL,

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(id)
);

CREATE TABLE Taski (
    id INTEGER PRIMARY KEY,
    zrobiony BOOLEAN NOT NULL,
    pokoj INTEGER NOT NULL,
    deadline DATE, -- task bez deadline'a może mieć deadline == null
    
    canvas_x REAL,
    canvas_y REAL,

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(id)
);

CREATE TABLE KolejnoscTaskow (
    id INTEGER PRIMARY KEY,
    task integer NOT NULL,
    task_wymagany INTEGER NOT NULL,

    CONSTRAINT task FOREIGN KEY (task) REFERENCES Taski(id),
    CONSTRAINT task_wymagany FOREIGN KEY (task_wymagany) REFERENCES Taski(id)
);

CREATE TABLE KluczeDoPokojow (
    id INTEGER PRIMARY KEY,
    pokoj INTEGER NOT NULL,
    uzytkownik VARCHAR(255) NOT NULL,
    klucz_publiczny VARCHAR(64), -- todo: ustalić jak długi jest szyfr
    klucz_prywatny VARCHAR(64),

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(id),
    CONSTRAINT uzytkownik FOREIGN KEY (uzytkownik) REFERENCES Uzytkownicy(nazwa)
);