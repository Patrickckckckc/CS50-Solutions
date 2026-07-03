CREATE TABLE passengers(
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age > 0)

);

CREATE TABLE check_ins(
    date DATETIME NOT NULL,
    passenger_id INTEGER NOT NULL,
    flight_id INTEGER NOT NULL,
    FOREIGN KEY(passenger_id) REFERENCES passengers(id),
    FOREIGN KEY(flight_id) REFERENCES flights(id)

);
CREATE TABLE airlines(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    concourse TEXT NOT NULL CHECK(concourse IN ('A', 'B', 'C', 'D', 'E', 'F', 'T'))

);

CREATE TABLE flights(
    id INTEGER PRIMARY KEY,
    flight_number TEXT NOT NULL,
    airline_id INTEGER NOT NULL,
    departing_code TEXT NOT NULL,
    heading_code TEXT NOT NULL,
    departure_date DATETIME NOT NULL,
    arrival_date DATETIME,
    FOREIGN KEY(airline_id) REFERENCES airlines(id)

);
