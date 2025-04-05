from user import User

class Student(User):
    course_id : str
    def __init__(self, id, first_name: str, last_name: str, cellphone: str,course_code):
        super().__init__(id, first_name, last_name, cellphone)
        self.course_id = course_code

    def create_student(self):
        return (f"INSERT INTO student (id,first_name,last_name,cellphone) VALUES({self.id}, '{self.first_name}',"
                f"'{self.last_name}', '{self.last_name}')")

    def get_student(self,id:int) :
        return f"SELECT * WHERE id = {id}"

    def update_student(self,id,first_name,last_name):
        return (f"UPDATE student "
                f"SET first_name = '{first_name}', last_name = '{last_name}'")