from lib.cohort import Cohort

#when i construct a cohort object it creates with the correct properties
def test_construct_cohort():
    cohort = Cohort(1, 'Sam', '1922-02-02',[])
    assert cohort.id == 1
    assert cohort.name == 'Sam'
    assert cohort.starting_date == '1922-02-02'
    assert cohort.students == []

"""
We can format cohorts to strings nicely
"""
def test_cohorts_format_nicely():
    cohort = Cohort(1, 'Sam', '1922-02-02', [])
    assert str(cohort) == "Cohort(1, Sam, 1922-02-02, [])"

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    cohort1 = Cohort(1, 'Sam', '1922-02-02', [])
    cohort2 = Cohort(1, 'Sam', '1922-02-02', [])
    assert cohort1 == cohort2