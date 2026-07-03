-- In 5.sql, write a SQL query to find all teams that Satchel Paige played for.

-- Your query should return a table with a single column, one for the name of the teams.

SELECT DISTINCT teams.name AS 'TEAMS' FROM teams JOIN performances ON teams.id = performances.team_id
JOIN players ON performances.player_id = players.id WHERE players.id = (
    SELECT id FROM players WHERE first_name = 'Satchel' AND last_name = 'Paige'
);
