CREATE VIEW frequently_reviewed AS
SELECT COUNT(reviews.id) AS total_reviews,
       listings.id,
       listings.property_type,
       listings.host_name
FROM reviews
JOIN listings
  ON reviews.listing_id = listings.id
GROUP BY listings.id
ORDER BY total_reviews DESC, listings.host_name
LIMIT 100;
