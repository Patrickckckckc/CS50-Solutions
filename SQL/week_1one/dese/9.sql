--In 9.sql, write a SQL query to find the name (or names) of the school district(s)
--with the single least number of pupils. Report only the name(s).
SELECT districts.name FROM schools
JOIN districts ON schools.district_id = districts.id
JOIN expenditures ON districts.id = expenditures.district_id
WHERE pupils = (
    SELECT MIN(pupils) FROM expenditures
)
GROUP BY districts.id
;
