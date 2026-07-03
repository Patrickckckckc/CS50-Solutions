CREATE VIEW june_vacancies AS
SELECT l.id,
       l.property_type,
       l.host_name,
       COUNT(a.date) AS days_vacant
FROM listings l
JOIN availabilities a
  ON l.id = a.listing_id
WHERE a.available = 1
  AND a.date BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY l.id, l.property_type, l.host_name;
