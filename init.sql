-- init.sql
CREATE TABLE example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO example_table (name) VALUES ('Test Data');