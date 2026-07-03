CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE schools (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    school_type TEXT NOT NULL CHECK(
        school_type IN (
            'Elementary School',
            'Middle School',
            'High School',
            'Lower School',
            'Upper School',
            'College',
            'University'
        )
    ),
    location TEXT NOT NULL,
    year_founded INTEGER NOT NULL
);

CREATE TABLE companies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    industry TEXT NOT NULL,
    location TEXT NOT NULL
);



CREATE TABLE people_connect(
    user_id_1 INTEGER NOT NULL,
    user_id_2 INTEGER NOT NULL,
    PRIMARY KEY (user_id_1, user_id_2),
    FOREIGN KEY (user_id_1) REFERENCES users(id)
    FOREIGN KEY(user_id_2) REFERENCES users(id)
);


CREATE TABLE school_connect(
    user_id INTEGER NOT NULL,
    school_id INTEGER NOT NULL,
    start_date_affiliation DATETIME NOT NULL,
    end_date_affiliation DATETIME,
    degree_type TEXT NOT NULL CHECK(degree_type in ('BA', 'MA', 'PhD')),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(school_id) REFERENCES schools(id)
);

CREATE TABLE company_connect(
    user_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    start_date_affiliation DATETIME NOT NULL,
    end_date_affiliation DATETIME,
    title TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(company_id) REFERENCES companies(id)
)
;
