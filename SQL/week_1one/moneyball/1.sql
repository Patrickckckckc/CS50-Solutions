-- In 1.sql, write a SQL query to find the average player salary by year.
-- Sort by year in descending order.
-- Round the salary to two decimal places and call the column “average salary”.
-- Your query should return a table with two columns, one for year and one for average salary.

SELECT ROUND(AVG(salary),2) AS 'Average Salary', year FROM salaries GROUP BY year ORDER BY year DESC;
