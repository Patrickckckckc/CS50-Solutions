-- Give me School Name and Distric name
SELECT schools.name AS "School", districts.name AS "District" FROM schools JOIN districts ON schools.district_id = districts.id;
