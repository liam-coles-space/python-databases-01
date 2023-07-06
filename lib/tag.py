class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    
    def __repr__(self):
        return f"Tag({self.id}, {self.name})"
    
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__