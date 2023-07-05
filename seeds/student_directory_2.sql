-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;

DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('spring 23', to_date('2023-03','yyyy-mm'));
INSERT INTO cohorts (name, starting_date) VALUES ('winter 22', to_date('2022-12','yyyy-mm'));
INSERT INTO cohorts (name, starting_date) VALUES ('summer 22', to_date('2022-08','yyyy-mm'));
INSERT INTO cohorts (name, starting_date) VALUES ('summer 23', to_date('2023-06','yyyy-mm'));

INSERT INTO students (name, cohort_id) VALUES ('student1', 1);
INSERT INTO students (name, cohort_id) VALUES ('student2', 2);
INSERT INTO students (name, cohort_id) VALUES ('student3', 1);
INSERT INTO students (name, cohort_id) VALUES ('student4', 3);
INSERT INTO students (name, cohort_id) VALUES ('student5', 3);
INSERT INTO students (name, cohort_id) VALUES ('student6', 2);
INSERT INTO students (name, cohort_id) VALUES ('student7', 2);
INSERT INTO students (name, cohort_id) VALUES ('student8', 1);
INSERT INTO students (name, cohort_id) VALUES ('student9', 4);
INSERT INTO students (name, cohort_id) VALUES ('student10', 1);
INSERT INTO students (name, cohort_id) VALUES ('student11', 4);
INSERT INTO students (name, cohort_id) VALUES ('student12', 4);


