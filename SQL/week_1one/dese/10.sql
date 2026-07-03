-- In 10.sql, write a SQL query to find the 10 public school districts with the highest per-pupil expenditures.
-- Your query should return the names of the districts and the per-pupil expenditure for each.

SELECT DISTINCT districts.name, per_pupil_expenditure FROM schools
JOIN districts ON schools.district_id = districts.id
JOIN expenditures ON districts.id = expenditures.district_id
WHERE districts.type = 'Public School District'
ORDER BY per_pupil_expenditure DESC LIMIT 10
;
