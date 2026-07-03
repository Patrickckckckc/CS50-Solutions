CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    password VARCHAR(15) NOT NULL
);

CREATE TABLE schools(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type ENUM('Primary', 'Secondary', 'Higher Education'),
    location VARCHAR(50) NOT NULL,
    year_founded YEAR NOT NULL
);

CREATE TABLE companies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL,
    type ENUM('Technology', 'Education', 'Business')
);

CREATE TABLE user_connection(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    user_id2 INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(user_id2) REFERENCES users(id),
    UNIQUE (user_id, user_id2)
);

CREATE TABLE school_connection(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    school_id INT NOT NULL,
    start_affiliation DATE NOT NULL,
    end_affiliation DATE NOT NULL,
    degree ENUM('BA', 'MA', 'PhD'),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(school_id) REFERENCES schools(id),
    UNIQUE(user_id, school_id, degree)
);

CREATE TABLE company_connection(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    company_id INT NOT NULL,
    start_affiliation DATE NOT NULL,
    end_affiliation DATE NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(company_id) REFERENCES companies(id),
    UNIQUE(user_id, company_id)
);


INSERT INTO users (first_name, last_name, password) VALUES ('Claudine', 'Gay', 'password');
INSERT INTO users (first_name, last_name, password) VALUES ('Reid', 'Hoffman', 'password');
INSERT INTO schools (name, location, year_founded) VALUES ('Harvard University', 'Cambridge, Massachusetts', 1901);
UPDATE schools SET type = 'Higher Education' WHERE name = 'Harvard University';
INSERT INTO companies (name, location, type) VALUES ('LinkedIn', 'Sunnyvale, California', 'Technology');
--Claudine Gay’s connection with Harvard, pursuing a PhD from January 1st, 1993, to December 31st, 1998.
INSERT INTO school_connection(user_id, school_id, start_affiliation, end_affiliation, degree)
VALUES(
    (SELECT id FROM users WHERE first_name = 'Claudine' AND last_name = 'Gay'),
    (SELECT id FROM schools WHERE name = 'Harvard University'),
    '1993-01-01',
    '1998-12-31',
    'PhD'
);
--Reid Hoffman’s connection with LinkedIn, with title “CEO and Chairman”, from January 1st, 2003 to February 1st, 2007
