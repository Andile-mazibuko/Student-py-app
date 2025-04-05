import DataBase
from Student import Student

DataBase.create_table()
#stud = Student(id=1234,first_name="andile",last_name="mazibuko",cellphone="0123456789",course_code="DPRS20")
#DataBase.__create__stud(stud)
print(DataBase.__get__Stud(1234))