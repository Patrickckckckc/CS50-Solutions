-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database
-- Find all the games that an user has
SELECT games.name FROM games
JOIN library ON library.game_id = games.id
WHERE user_id = (
    SELECT id FROM users WHERE username = "patrick"
);


-- Find all the Friend Information of an User
SELECT username, status, created_at FROM friends
JOIN users ON friends.friend_id = users.id
WHERE user_id = (
    SELECT id FROM users WHERE username = "patrick"
);

-- Find top 10 Most played games by time
SELECT name, hours_played FROM games
JOIN session ON session.game_id = games.id
GROUP BY game_id
ORDER BY hours_played DESC
LIMIT 10;

---- Add a new user
INSERT INTO "users" ("username", "total_games")
VALUES ('patrick', 12);

-- Add a new game
INSERT INTO "games" ("name", "company", "type")
VALUES ('Half-Life 2', 'Valve', 'Shooter');

-- Add a new friendship
INSERT INTO "friends" ("user_id", "friend_id", "status", "created_at")
VALUES (1, 2, 'accepted', '2026-03-01 10:15:00');

-- Add a new library record (user owns a game)
INSERT INTO "library" ("user_id", "game_id", "purchase_date")
VALUES (1, 1, '2026-02-01 10:00:00');

-- Add a new session (user plays a game)
INSERT INTO "session" ("user_id", "game_id", "last_session", "hours_played")
VALUES (1, 1, '2026-03-01 10:30:00', 25);
