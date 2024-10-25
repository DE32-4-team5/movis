CREATE TABLE MOVIS_TBL (
    ID          INT NOT NULL AUTO_INCREMENT,
    movieCd	INT,
    movieNm	VARCHAR(50),
    movieNmEn	VARCHAR(50),
    openDt	DATE,
    repGenreNm	VARCHAR(10),
    repNationNm	VARCHAR(20),
    peopleNm	VARCHAR(30),
    PRIMARY KEY (ID)
);
