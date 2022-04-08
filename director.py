from person import Person

class Director(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_fullname(self):
        return self.first_name + " " + self.last_name