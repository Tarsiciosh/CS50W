CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    detination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);