import DataBase,random
from Student import Student


#stud = Student(id=125534,first_name="andile",last_name="mazibuko",cellphone="0123456789",course_code="DPRS20")
#DataBase.__create__stud(stud)
#print(DataBase.__get__stud(1234))
#DataBase.__update__student(Student(125534,"Harry","Kane","0123456789","DPRS20"))
#print(DataBase.__get_all()[2][2])
#DataBase.__delete_stud(stud)
choice = int(input("Please select from the below optios \n 1- Register Account \n 2 - Update your accout \n 3- View Other students \n 0 - exit\n = "))

#random.choice(range(0,10000))
while choice != 0:
    if choice == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        cellphone = input("Cellphone: ")
        course_code = input("Course code: ")

        stud = Student(id=random.choice(range(0,10000)),first_name=first_name,last_name=last_name,cellphone=cellphone,course_code=course_code)
        DataBase.__create__stud(stud)
    choice = int(input("Please select from the below optios \n 1- Register Account \n 2 - Update your accout \n 3- View Other students \n 0 - exit\n = "))
