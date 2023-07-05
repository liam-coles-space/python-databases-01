As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Table design:

Nouns:
names, cohort, student, starting_dates

Record  |   Properties
Cohort      Name, starting date   
Student     Name

Table: Cohorts
id: serial
name: text
starting_date: date

Table: Students
id:serial
name: text

Can one COHORTS have many Students? (Yes)
Can one STUDENTS have many COHORTS? (No)


-> Therefore,
-> An cohort HAS MANY students
-> An student BELONGS TO an cohort

-> Therefore, the foreign key is on the students table.


CREATE TABLE cohorts(
    id SERIAL PRIMARY KEY,
    name text,
    starting_date date
);

CREATE TABLE students(
    student_id SERIAL PRIMARY KEY
    name text
    cohort_id int,
    constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

