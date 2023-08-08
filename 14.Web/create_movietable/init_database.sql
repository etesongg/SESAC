DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(30) NOT NULL,
    grade Real,
    sales_rate Real
);