
CREATE TABLE "meteorites" (
    -- TODO
    name TEXT NOT NULL,
    id INTEGER PRIMARY KEY,
    class TEXT NOT NULL,
    mass REAL,
    discovery TEXT CHECK(discovery IN('Fell', 'Found')),
    year INTEGER,
    lat REAL,
    long REAL
);

CREATE TABLE "meteorites_temp"(
    -- TODO
    name TEXT NOT NULL,
    id INTEGER,
    nametype TEXT NOT NULL,
    class TEXT NOT NULL,
    mass REAL,
    discovery TEXT CHECK(discovery IN('Fell', 'Found')),
    year INTEGER,
    lat REAL,
    long REAL
);




.import --csv --skip 1 meteorites.csv meteorites_temp
SELECT * FROM meteorites_temp LIMIT 10;
UPDATE meteorites_temp SET mass = ROUND(mass, 2), lat = ROUND(lat,2), long = ROUND(long,2);
UPDATE meteorites_temp SET mass = NULL WHERE mass = 0;
UPDATE meteorites_temp SET lat = NULL WHERE lat = 0;
UPDATE meteorites_temp SET long = NULL WHERE long = 0;


SELECT * FROM meteorites_temp WHERE nametype LIKE '%Relic%';
DELETE FROM meteorites_temp WHERE nametype LIKE '%Relic%';
ALTER TABLE meteorites_temp DROP COLUMN nametype;
ALTER TABLE meteorites_temp DROP COLUMN id;


INSERT INTO meteorites ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long"
FROM "meteorites_temp"
ORDER BY "year" ASC, "name";


