-- drop necessary tables and sequences
DROP TABLE IF EXISTS descriptions CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS subjects CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS descriptions_id_seq;
DROP SEQUENCE IF EXISTS tasks_id_seq;
DROP SEQUENCE IF EXISTS subjects_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- user table = stores personal user information
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
);

-- subjects table = stores all subjects relating to users
CREATE SEQUENCE IF NOT EXISTS subjects_id_seq;
CREATE TABLE subjects(
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(255),
    user_id INTEGER,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) 
    REFERENCES users(id) ON DELETE CASCADE
);

-- tasks table = stores all tasks relating to subjects
CREATE SEQUENCE IF NOT EXISTS tasks_id_seq;
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    task_name VARCHAR(255),
    task_description VARCHAR(10000),
    subject_id INTEGER,
    CONSTRAINT fk_subject_id FOREIGN KEY (subject_id) 
    REFERENCES subjects(id) ON DELETE CASCADE
);
