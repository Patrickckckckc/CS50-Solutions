-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it
-- Represent users on STEAM
CREATE TABLE "users" (
    "id" INTEGER,
    "username" TEXT NOT NULL,
    "total_games" INTEGER CHECK(total_games >= 0),
    PRIMARY KEY("id")
);

-- Represent games on STEAM
CREATE TABLE "games" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "company" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    PRIMARY KEY("id")
);

-- Represent relationship between USERS
CREATE TABLE "friends" (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "friend_id" INTEGER NOT NULL,
    "status" TEXT CHECK(status IN ('pending','accepted','blocked')),
    "created_at" DATETIME NOT NULL,

    PRIMARY KEY("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("friend_id") REFERENCES "users"("id")
);

-- Represent the games in the library of a user
CREATE TABLE "library" (
    "user_id" INTEGER,
    "game_id" INTEGER,
    "purchase_date" DATETIME NOT NULL,
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("game_id") REFERENCES "games"("id")
);

-- Represent the session that an user have with a game
CREATE TABLE "session" (
    "user_id" INTEGER,
    "game_id" INTEGER,
    "last_session" DATETIME NOT NULL,
    "hours_played" INTEGER CHECK(hours_played >= 0),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY("game_id") REFERENCES "games"("id")
);


CREATE VIEW "games_on_library_patrick"
AS SELECT games.name FROM games
JOIN library ON library.game_id = games.id
WHERE user_id = (
    SELECT id FROM users WHERE username = "patrick"
);
