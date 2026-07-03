-- In 12.sql, write a SQL query to find the players among the 10 least expensive players per hit
-- and among the 10 least expensive players per RBI in 2001.

-- Your query should return a table with two columns, one for the players’ first names and one of their last names.
-- You can calculate a player’s salary per RBI by dividing their 2001 salary by their number of RBIs in 2001.
-- You may assume, for simplicity, that a player will only have one salary and one performance in 2001.
-- Order your results by player ID, least to greatest (or alphabetically by last name, as both are the same in this case!).

SELECT first_name, last_name
FROM (
    SELECT first_name, last_name, (salary /H) AS cost_per_hit
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE performances.year = 2001
      AND performances.year = salaries.year
      AND H != 0
    ORDER BY cost_per_hit ASC, first_name, last_name
    LIMIT 10
) AS per_hit

INTERSECT

SELECT first_name, last_name
FROM (
    SELECT first_name, last_name, (salary / RBI) AS cost_per_rbi
    FROM players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id
    WHERE performances.year = 2001
      AND performances.year = salaries.year
      AND RBI != 0
    ORDER BY cost_per_rbi ASC, first_name, last_name
    LIMIT 10
) AS per_rbi;


