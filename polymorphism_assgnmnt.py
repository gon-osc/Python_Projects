#Parent class

class User:
    name = 'Nick'
    email = 'nick1@gmail.com'
    password = '789xyz'


    def getLoginInfo(self) :
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_password = input('Enter your password: ')
        if (entry_email == self.email and entry_password == self.password) :
            print('Welcome back, {}!'.format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child class

class Teacher(User) :
    department = 'History & Archeology'
    teacher_aide = 'Mark'
    pin_number = '2020'


    def getLoginInfo(self) :
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_pin = input('Enter your pin: ')
        if (entry_email == self.email and entry_pin == self.pin_number) :
            print('Welcome back, {}!'.format(entry_name))
        else:
            print("The password or email is incorrect.")

                

class Student(User) :
    subject_class = 'History'
    studentId = '56789'


    def getLoginInfo(self) :
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email: ')
        entry_studentId = input('Enter your StudentID: ')
        if (entry_email == self.email and entry_studentId == self.studentId) :
            print('Welcome back, {}!'.format(entry_name))
        else:
            print("Your Student ID or email is incorrect.")





employee = Teacher()
employee.getLoginInfo()


undergraduate = Student()
undergraduate.getLoginInfo()





     
    
