
-- *** The Lost Letter ***
SELECT DISTINCT address, type FROM addresses JOIN packages ON addresses.id = packages.to_address_id JOIN scans ON packages.to_address_id =
scans.package_id WHERE contents = 'Congratulatory letter' AND action = 'Drop';

-- *** The Devious Delivery ***
SELECT contents FROM packages
WHERE from_address_id IS NULL;

SELECT type FROM addresses WHERE id = (SELECT address_id FROM scans
WHERE action = 'Drop' AND package_id = (
    SELECT id FROM packages WHERE contents = (
        SELECT contents FROM packages
        WHERE from_address_id IS NULL
    )
));


-- *** The Forgotten Gift ***
SELECT contents
FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address LIKE '%109 Tileston Street%'
);


SELECT name FROM drivers WHERE id = (SELECT driver_id FROM scans
WHERE timestamp = (SELECT timestamp FROM scans WHERE package_id = (SELECT id FROM packages
WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address LIKE '%109 Tileston Street%'
)))
AND package_id = (SELECT id FROM packages WHERE from_address_id = (
    SELECT id
    FROM addresses
    WHERE address LIKE '%109 Tileston Street%'
))
);
