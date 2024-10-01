class Person:
    def __init__(self, id) -> None:
        self.id = id
some_person = Person(100)
some_person.__dict__['age'] = 30
print(some_person.age + len(some_person.__dict__))