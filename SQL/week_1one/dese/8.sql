-- In 8.sql, write a SQL query to display the names of all school districts and the number of pupils enrolled in each.
SELECT districts.name, pupils AS "total_pupils" FROM schools JOIN districts ON schools.district_id = districts.id
JOIN expenditures ON districts.id = expenditures.district_id GROUP BY districts.id;
