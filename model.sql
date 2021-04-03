CREATE TABLE Vid_jil (
       Kod_vida             INTEGER NOT NULL
                                   CHECK (Kod_vida>0),
       Naim_jil             VARCHAR(50) NOT NULL,
       PRIMARY KEY (Kod_vida)
);


CREATE TABLE Kateg_kvart (
       Kod_kategorii        INTEGER NOT NULL
                                   CHECK (Kod_kategorii>0),
       Naim_kat             VARCHAR(50) NOT NULL,
       PRIMARY KEY (Kod_kategorii)
);


CREATE TABLE Sotrudn (
       Kod_sotrudn          INTEGER NOT NULL
                                   CHECK (Kod_sotrudn>0),
       FIO                  VARCHAR(90) NOT NULL,
       Dolz                 VARCHAR(70) NOT NULL,
       PRIMARY KEY (Kod_sotrudn)
);


CREATE TABLE Client (
       Kod_client           INTEGER NOT NULL
                                   CHECK (Kod_client>0),
       Pasp                 VARCHAR(40) NOT NULL,
       FIO_client                  VARCHAR(70) NOT NULL,
       Phone                VARCHAR(50) NOT NULL,
       Status               VARCHAR(20) NOT NULL,
       PRIMARY KEY (Kod_client)
);


CREATE TABLE Zayavka (
       ID_zaya              SERIAL NOT NULL,
       Data_zaya            DATE NOT NULL,
       Opisanie             VARCHAR(20) NOT NULL,
       Kod_client           INTEGER NOT NULL
                                   CHECK (Kod_client>0),
       Kod_sotrudn          INTEGER NOT NULL
                                   CHECK (Kod_sotrudn>0),
       PRIMARY KEY (ID_zaya), 
       FOREIGN KEY (Kod_sotrudn)
                             REFERENCES Sotrudn  (Kod_sotrudn)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT, 
       FOREIGN KEY (Kod_client)
                             REFERENCES Client  (Kod_client)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF1Zayavka ON Zayavka
(
       Kod_client ASC
);

CREATE INDEX XIF2Zayavka ON Zayavka
(
       Kod_sotrudn ASC
);


CREATE TABLE Dogovor_prod (
       Id_dog               SERIAL NOT NULL,
       Num_dog              INTEGER NOT NULL
                                   CHECK (Num_dog>0),
       Date_sost            DATE NOT NULL,
       Date_prod            DATE NOT NULL,
       Sum_dog              NUMERIC(9,2) DEFAULT 0
                                   CHECK (Sum_dog>=0),
       Opl                  NUMERIC(9,2) DEFAULT 0
                                   CHECK (Opl>=0),
       ID_zaya              INTEGER NOT NULL,
       Kod_sotrudn          INTEGER NOT NULL
                                   CHECK (Kod_sotrudn>0),
       PRIMARY KEY (Id_dog), 
       FOREIGN KEY (Kod_sotrudn)
                             REFERENCES Sotrudn  (Kod_sotrudn)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT, 
       FOREIGN KEY (ID_zaya)
                             REFERENCES Zayavka  (ID_zaya)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF11Dogovor_prod ON Dogovor_prod
(
       ID_zaya ASC
);

CREATE INDEX XIF12Dogovor_prod ON Dogovor_prod
(
       Kod_sotrudn ASC
);


CREATE TABLE Obj_zastroi (
       Num_obj              INTEGER NOT NULL
                                   CHECK (Num_obj>=0),
       Street               VARCHAR(70) NOT NULL,
       Num_zd               VARCHAR(20) NOT NULL,
       Kol_vo_et            INTEGER NOT NULL DEFAULT 1
                                   CHECK (Kol_vo_et>0),
       Kod_vida             INTEGER NOT NULL
                                   CHECK (Kod_vida>0),
       PRIMARY KEY (Num_obj), 
       FOREIGN KEY (Kod_vida)
                             REFERENCES Vid_jil  (Kod_vida)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF1Obj_zastroi ON Obj_zastroi
(
       Kod_vida ASC
);


CREATE TABLE Kvart (
       Id_kv                SERIAL NOT NULL,
       Num_etag             INTEGER NOT NULL
                                   CHECK (Num_etag>0),
       Num_kv               VARCHAR(50) NOT NULL,
       Kol_vo_kom           INTEGER DEFAULT 1
                                   CHECK (Kol_vo_kom>0),
       Area                 NUMERIC(6,2) DEFAULT 0
                                   CHECK (Area>0),
       Stoim                NUMERIC(9,2) DEFAULT 0
                                   CHECK (Stoim>=0),
       Num_obj              INTEGER NOT NULL
                                   CHECK (Num_obj>=0),
       Kod_kategorii        INTEGER NOT NULL
                                   CHECK (Kod_kategorii>0),
       PRIMARY KEY (Id_kv), 
       FOREIGN KEY (Kod_kategorii)
                             REFERENCES Kateg_kvart  (Kod_kategorii)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT, 
       FOREIGN KEY (Num_obj)
                             REFERENCES Obj_zastroi  (Num_obj)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF7Kvart ON Kvart
(
       Num_obj ASC
);

CREATE INDEX XIF8Kvart ON Kvart
(
       Kod_kategorii ASC
);


CREATE TABLE Prod_kv (
       Id_prod              SERIAL NOT NULL,
       Id_dog               INTEGER NOT NULL,
       Id_kv                INTEGER NOT NULL,
       Stoim                NUMERIC(6,2) DEFAULT 0
                                   CHECK (Stoim>=0),
       PRIMARY KEY (Id_prod), 
       FOREIGN KEY (Id_dog)
                             REFERENCES Dogovor_prod  (Id_dog)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT, 
       FOREIGN KEY (Id_kv)
                             REFERENCES Kvart  (Id_kv)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF6Prod_kv ON Prod_kv
(
       Id_kv ASC
);

CREATE INDEX XIF7Prod_kv ON Prod_kv
(
       Id_dog ASC
);


CREATE TABLE Kn_oplat (
       Id_oplt              SERIAL NOT NULL,
       Date_opl             DATE NOT NULL,
       Sum_opl              INTEGER DEFAULT 0
                                   CHECK (Sum_opl>=0),
       Id_dog               INTEGER NOT NULL,
       PRIMARY KEY (Id_oplt), 
       FOREIGN KEY (Id_dog)
                             REFERENCES Dogovor_prod  (Id_dog)
                             ON DELETE RESTRICT
                             ON UPDATE RESTRICT
);

CREATE INDEX XIF11Kn_oplat ON Kn_oplat
(
       Id_dog ASC
);