from lib.student import Student

#when i construct a student object it creates with the correct properties
def test_student_constructs():
    student = Student(1, 'Liam', 1)
    assert student.id == 1
    assert student.name == 'Liam'
    assert student.cohort_id == 1


"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    student = Student(1, 'Liam', 1)
    assert str(student) == "Student(1, Liam, 1)"

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    student1 = Student(1, 'Liam', 1)
    student2 = Student(1, 'Liam', 1)
    assert student1 == student2



