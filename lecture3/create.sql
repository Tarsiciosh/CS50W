CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    detination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

--\d  (list the tables in the database)

INSERT INTO flights (origin, detination, duration) VALUES ('Paris','New York',540);
INSERT INTO flights (origin, detination, duration) VALUES ('Tokyo','Shanghai',185);
INSERT INTO flights (origin, detination, duration) VALUES ('Seoul','Mexico City',825);
INSERT INTO flights (origin, detination, duration) VALUES ('Mexico City','Lima',350);
INSERT INTO flights (origin, detination, duration) VALUES ('Hong Kong','Shanghai',130);


SELECT origin, detination FROM flights WHERE id =3;

SELECT * FROM flights WHERE duration > 500 AND detination = 'Paris';

SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'New York';

SELECT COUNT(*) FROM flights;

SELECT COUNT(*) FROM flights WHERE origin = 'New York';

SELECT MIN(duration) FROM flights;

SELECT * FROM flights WHERE duration = 130;

SELECT * FROM flights WHERE origin IN ('Paris','Hong Kong');

SELECT * FROM flights WHERE origin LIKE '%a%';

UPDATE flights 
    SET duration = 430
    WHERE origin = 'Paris'
    AND detination = 'New York';


DELETE FROM flights WHERE detination = 'Madrid';

SELECT * FROM flights LIMIT 2;

SELECT * FROM flights ORDER BY duration ASC LIMIT 3;

SELECT origin , COUNT(*) FROM flights GROUP BY origin;

SELECT origin , COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice',1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob',4);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie',4);
INSERT INTO passengers (name, flight_id) VALUES ('David',6);
INSERT INTO passengers (name, flight_id) VALUES ('Tom',6);
INSERT INTO passengers (name, flight_id) VALUES ('Eric',4);

SELECT origin, detination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id; 

SELECT origin, detination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';

SELECT origin, detination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id; 

SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;

SELECT * FROM flights WHERE id IN (
    SELECT flight_id FROM passengers 
    GROUP BY flight_id HAVING COUNT(*) > 1);

-- transactions
BEGIN 
COMMIT

-- open the psql from windows menu
-- always enter and then pass: ********
-- then the database is up and running
-- you can create tables insert and everything else