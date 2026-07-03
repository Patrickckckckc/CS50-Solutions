-- In 11.sql, write a SQL query to display the names of schools, their per-pupil expenditure,
-- and their graduation rate.
-- Sort the schools from greatest per-pupil expenditure to least.
-- If two schools have the same per-pupil expenditure, sort by school name.
-- You should assume a school spends the same amount per-pupil their district as a whole spends.

SELECT schools.name, per_pupil_expenditure, graduated FROM schools JOIN districts ON schools.district_id = districts.id
JOIN expenditures ON districts.id = expenditures.district_id JOIN graduation_rates ON schools.id = graduation_rates.school_id
ORDER BY per_pupil_expenditure DESC, schools.name ASC;
