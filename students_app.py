from lib.cohort_repository import *
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/student_directory_2.sql")

repository = CohortRepository(connection)
cohort = repository.find_with_students('winter 22')

print(cohort)



