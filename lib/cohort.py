class Cohort:
    def __init__(self, id, name, starting_date, students = None):
        self.id = id
        self.name = name
        self.starting_date = starting_date
        self.students = students or []

    def __repr__(self):
        return f"Cohort({self.id}, {self.name}, {self.starting_date}, {self.students})"
    
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__