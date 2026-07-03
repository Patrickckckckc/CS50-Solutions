-- Create Courses Index (35% BETTER)
CREATE INDEX course_search_department_number_semester_title
ON courses(department, number, semester, title);


-- NOT CREATE enrollments (NOT GOOD)
-- NOT CREATE satisfies is worse
