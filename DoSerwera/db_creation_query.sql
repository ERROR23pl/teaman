-- notes:
-- * some of these varchars may have to change to TEXT datatype
-- * if varchar is used, maybe try to make some kind of wrapper around the string to make sure no bugs can crawl up

-- todo: add AUTOINCREMENT to every id
-- todo: check if hash length == 128. If not change the varchars.
-- todo: Jak długi jest klucz publiczny? Zmienić w miejsach ! KEY

-- to może być publiczne, przecież to nie są nasze informacje
CREATE TABLE Role (
    nazwa VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Uzytkownicy (
    nazwa VARCHAR(128), -- nazwa_publiczna
    login VARCHAR(128), --! HASH
    haslo VARCHAR(128), --! HASH
    token VARCHAR(128), --! HASH
    rola VARCHAR(255) NOT NULL,
    last_update TIME,

    -- ! klucz publiczny jest null tylko i wyłącznie pomiędzy stworzeniem użytkowanika a zaakceptowaniem klucza przez serwer (unique)
    klucz_publiczny TEXT UNIQUE, -- ! KEY

    CONSTRAINT rola FOREIGN KEY (rola) REFERENCES Role(nazwa)
);

CREATE TABLE KodyZaproszeniowe (
    kod VARCHAR(128) PRIMARY KEY, -- ! HASH
    data_dodania DATE NOT NULL
);

CREATE TABLE Pokoje (
    nazwa VARCHAR(255) PRIMARY KEY
);

CREATE TABLE KluczeDoPokojow (
    id INTEGER,
    pokoj VARCHAR(255) NOT NULL,
    uzytkownik VARCHAR(128) NOT NULL,
    klucz_publiczny TEXT, -- todo: klucz zaszyfrowany kluczem, jaką ma długość? (jak niewiadomo to TEXT)
    klucz_prywatny TEXT, -- todo: klucz zaszyfrowany kluczem, jaką ma długość? (jak niewiadomo to TEXT)

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa),
    CONSTRAINT uzytkownik FOREIGN KEY (uzytkownik) REFERENCES Uzytkownicy(login)
);

CREATE TABLE CzlonkowiePokojow (
    id INTEGER,
    uzytkownik VARCHAR(128) NOT NULL,
    pokoj VARCHAR(255) NOT NULL,

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT uzytkownik FOREIGN KEY (uzytkownik) REFERENCES Uzytkownicy(login),
    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa)
);

CREATE TABLE Wiadomosci (
    id INTEGER,
    pokoj VARCHAR(255) NOT NULL,
    tresc TEXT NOT NULL, --! ENCODED
    data_wyslania TIME NOT NULL,
    autor VARCHAR(128) NOT NULL,

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT autor FOREIGN KEY (autor) REFERENCES Uzytkownicy(nazwa),
    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa)
);


CREATE TABLE Wydarzenia (
    id INTEGER,
    pokoj VARCHAR(255) NOT NULL,
    nazwa VARCHAR(255) NOT NULL UNIQUE, -- ! ENCODED
    data DATE NOT NULL,

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa)
);

CREATE TABLE Taski (
    id INTEGER,
    tekst TEXT, --! ENCODED
    zrobiony BOOLEAN NOT NULL,
    pokoj VARCHAR(255) NOT NULL,
    deadline DATE, -- task bez deadline'a może mieć deadline == NULL
    
    canvas_x REAL,
    canvas_y REAL,

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa)
);

CREATE TABLE KolejnoscTaskow (
    id INTEGER,
    task INTEGER NOT NULL,
    task_wymagany INTEGER NOT NULL, -- todo: check if task != task_wymagany.

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT task FOREIGN KEY (task) REFERENCES Taski(id),
    CONSTRAINT task_wymagany FOREIGN KEY (task_wymagany) REFERENCES Taski(id)
);

CREATE TABLE Pliki (
    id INTEGER,
    nazwa_pliku TEXT, --! ENCODED
    pokoj VARCHAR(255) NOT NULL,
    autor VARCHAR(128) NOT NULL,
    zawartosc LONGBLOB NOT NULL,

    PRIMARY KEY(id AUTOINCREMENT),

    CONSTRAINT pokoj FOREIGN KEY (pokoj) REFERENCES Pokoje(nazwa),
    CONSTRAINT autor FOREIGN KEY (autor) REFERENCES Uzytkownicy(nazwa)
);


INSERT INTO Role VALUES ("Admin");
INSERT INTO Role VALUES ("Uzytkownik");
INSERT INTO Role VALUES ("Grafik");
INSERT INTO Role VALUES ("Developer");
INSERT INTO Role VALUES ("Tester");
INSERT INTO Role VALUES ("Programista");
INSERT INTO Role VALUES ("Manager");
INSERT INTO Role VALUES ("Praktykant");
INSERT INTO Role VALUES ("Niezweryfikowany");