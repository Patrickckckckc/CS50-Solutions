-- The app’s user engagement team needs to identify active users. Find all usernames of users who have logged in since 2024-01-01.
-- Ensure your query uses the search_users_by_last_login index, which is defined as follows:

SELECT username FROM users
WHERE last_login_date >= '2024-01-01';
