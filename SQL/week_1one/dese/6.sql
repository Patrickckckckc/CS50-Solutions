-- In 6.sql, write a SQL query to find the names of schools (public or charter!) that reported a 100% graduation rate.
SELECT name FROM schools JOIN graduation_rates ON schools.id = graduation_rates.school_id WHERE graduated = 100;
