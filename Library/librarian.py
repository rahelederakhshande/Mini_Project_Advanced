from person import *
class Librarian(Person):
    last_id = 1000
    def __init__(self, name, age, employee_id):
        id_ = "L" + str(Librarian.last_id)
        super().__init__(name, age, id_)
        self.employee_id = employee_id
        Librarian.last_id += 1

    def introduce(self):
        return f"Librarian {self.name} Id: {self.employee_id}"