-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the Crime Description:
SELECT description FROM crime_scene_reports AS CRIME WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Theft of the CS50 duck took place at 10:15 a.m. at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time;
-- each of their interview transcripts mentions the bakery.

-- Lookinv for interviews
SELECT  name, transcript FROM interviews WHERE year = 2024 AND month = 7 AND day = 28;

-- Ruth -- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for
--cars that left the parking lot in that time frame

--Eugene -- Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

-- Raymond As the thief was leaving the bakery,
-- they called someone who talked to them for less than a minute.
--  I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- RUTH INFORMATION:
SELECT name, phone_number, passport_number FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate WHERE year == 2024 AND month = 7 AND day = 28 AND hour = 10 AND activity = 'exit' AND minute < 25 AND minute > 15;

-- Conection between the bakery_security_logs with person
-- FIRST LIST OF SUSPECTS: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey

-- EUGENE INFORMATION:
SELECT name, phone_number, passport_number FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE year = 2024 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- SECOND LIST OF SUSPECT: Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista

-- RAYMOND INFORMATION:
SELECT DISTINCT name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60;

-- THIRD LIST OF SUPECTS: Sofia, Kelsey, Bruce, Taylor, Diana, Carina, Kenny, Benista

-- BRUCE OR DIANA are the criminals
 -- Calculate flights, passengers -> FIND THE THIEF
SELECT name, people.id FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE passengers.passport_number IN (SELECT passport_number FROM passengers WHERE flights.id IN (SELECT id FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND hour < 10)) AND name IN ('Bruce', 'Diana');
 -- The THIEF IS BRUCE 686048

 --  FIND THE ACCOMPLICE WITH THE CALL reciever
SELECT name, caller FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE caller = (SELECT phone_number FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE passengers.passport_number IN (SELECT passport_number FROM passengers WHERE flights.id IN (SELECT id FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND hour < 10)) AND name IN ('Bruce', 'Diana')) AND year = 2024 AND month = 7 AND day = 28 AND duration < 60;
 -- The OTHER is ROBIN with phone (367) 555-5533

-- FIND THE DESTINATION
SELECT DISTINCT full_name, city FROM airports JOIN flights ON airports.id = flights.destination_airport_id WHERE airports.id = (SELECT DISTINCT destination_airport_id FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE flight_id = (SELECT flight_id FROM passengers WHERE passengers.passport_number = (SELECT people.passport_number FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id WHERE passengers.passport_number IN (SELECT passport_number FROM passengers WHERE flights.id IN (SELECT id FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND hour < 10)) AND name IN ('Bruce', 'Diana'))));

-- LaGuardia Airport New York City
SELECT DISTINCT full_name, city FROM people AS pe JOIN passengers AS pa ON pe.passport_number = pa.passport_number JOIN flights AS f ON pa.flight_Id = f.id JOIN airports AS a ON f.destination_airport_id = a.id WHERE year = 2024 AND month = 7 AND day = 29 AND hour < 10 AND name IN ('Bruce', 'Diana');
