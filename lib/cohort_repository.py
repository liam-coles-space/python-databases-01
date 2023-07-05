from lib.student import *
from lib.cohort import *
class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohort_name):
        rows = self._connection.execute(
            'select cohorts.id as id, cohorts.name as cohort_name, cohorts.starting_date as cohort_starting_date, students.id as student_id, students.name as student_name, students.cohort_id from cohorts join students on cohorts.id = students.cohort_id where cohorts.name = %s', [cohort_name]
        )
        students = []
        for row in rows:
            student = Student(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)   
      
        return Cohort(rows[0]["id"], rows[0]["cohort_name"], rows[0]["cohort_starting_date"], students)



