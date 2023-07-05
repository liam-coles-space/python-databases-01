from lib.cohort_repository import *
from lib.student import *
from lib.cohort import *
from datetime import date

#when i call the find_with_students methods I get the correct cohort object along with the correct list of student objects
def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students('winter 22')
    assert cohort == Cohort(2, 'winter 22', date(2022,12,1), [
        Student(2, 'student2', 2),
        Student(6, 'student6', 2),
        Student(7, 'student7', 2)
    ])


