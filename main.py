from Model.Student import Student
from Model.Teacher import Teacher
from Controller.Controller import Controller

controller = Controller()

controller.create_student(Student, "Иванов", "Иван", "Иванович")
controller.create_student(Student, "Петров", "Петр", "Петрович")
controller.create_student(Student, "Сидоров", "Артем", "Генадьевич")
controller.create_student(Student, "Ларионов", "Александр", "Петрович")
controller.create_student(Student, "Ибрагимов", "Егор", "Олегович")
controller.create_student(Student, "Иванов", "Артем", "Игоревич")
controller.create_teacher(Teacher, "Рыбин", "Валерий", "Александрович")
controller.create_teacher(Teacher, "Рыбин", "Александр", "Александрович")
controller.create_student_group(1,[1,2,3], "А")
controller.create_student_group(2,[4,5,6], "Б")
controller.get_all_student()
print('----------------------------------')
controller.get_all_teacher()
print('----------------------------------')
controller.get_user_by_id(Student,1)
print('----------------------------------')
controller.get_user_by_id(Teacher,1)
print('----------------------------------')
controller.get_all_student_group()
print('----------------------------------')
controller.get_group_by_id(1)





