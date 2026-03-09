import re
class employee():
    def __init__(self,id,name,age,mobile_no,email):
        self.id=id
        self.name=name
        self.age=age
        self.mobile_no = mobile_no
        self.email=email

class director(employee):
    def __init__(self,id,name,age,mobile_no,email,share):
        self.share=share
        super().__init__(id,name,age,mobile_no,email)

    def display(self):
        print(f'director - id:{self.id},name:{self.name},age:{self.age},mobile_no:{self.mobile_no},email:{self.email},share:{self.share}')

class manager(employee):
    def __init__(self,id,name,age,mobile_no,email,territory):
        self.territory=territory
        super().__init__(id,name,age,mobile_no,email)

    def display(self):
        print(f'manager - id:{self.id},name:{self.name},age:{self.age},mobile_no:{self.mobile_no},email:{self.email},territory:{self.territory}')

class teacher(employee):
    def __init__(self,id,name,age,mobile_no,email,subject):
        self.subject=subject
        super().__init__(id,name,age,mobile_no,email)

    def display(self):
        print(f'teacher - id:{self.id},name:{self.name},age:{self.age},mobile_no:{self.mobile_no},email:{self.email},subject:{self.subject}')

class EMS:
    def __init__(self):
        self.employees=[]


    def addemployee(self):
        print('1 DIRECTOR 2 MANAGER 3 TRAINER' )
        ch=int(input('Enter your choice: '))
        id=int(input('Enter employee id: '))
        name=input('Enter employee name: ')
        age=int(input('Enter employee age: '))
        mobile_no=int(input('enter employee mobile_no: '))
        email=input('Enter employee email: ')

        if ch=='1':
            share=float(input('Enter employee share: '))
            self.employees.append(director(id,name,age,mobile_no,email,share))
        elif ch=='2':
            territory=input('Enter employee territory: ')
            self.employees.append(manager(id,name,age,mobile_no,email,territory))
        elif ch=='3':
            subject=input('Enter employee subject: ')
            self.employees.append(teacher(id,name,age,mobile_no,email,subject))

        print('EMPLOYEE ADDED SUCCESSFULLY')

    def searchemployee(self):
        id=int(input('Enter employee id to search: '))
        for e in self.employees:
            if e.id==id:
                e.display()
                return
        print('EMPLOYEE NOT FOUND')

    def modifyemployee(self):
        id=int(input('Enter employee id to modify: '))
        for e in self.employees:
            if e.id==id:
                name=input('Enter employee name to update: ')
                age=int(input('Enter employee age to update: '))
                mobile_no=input('Enter employee mobile number to update: ')
                email=input('Enter employee email to update: ')

                if isinstance(e,director):
                    e.share=float(input('Enter employee share to update: '))
                elif isinstance(e,manager):
                    e.territory=input('Enter employee territory to update: ')
                else:
                    e.subject=input('Enter employee subject to update: ')
                print('EMPLOYEE UPDATED SUCCESSFULLY')
                return
        print('EMPLOYEE NOT FOUND')

    def deleteemployee(self):

        id=int(input('Enter employee id to delete: '))
        for e in self.employees:
            if e.id==id:
                self.employees.remove(e)
                print('EMPLOYEE DELETED SUCCESSFULLY')
                return
        print('EMPLOYEE NOT FOUND')

    def displayemployee(self):
        if not self.employees:
            print('EMPLOYEE NOT FOUND')
            return
        for e in self.employees:
            e.display()
ems=EMS()
while (1):
    print('1. ADD EMPLOYEE\n 2 SEARCH EMPLOYEE\n 3 MODIFY EMPLOYEE\n 4 DELETE EMPLOYEE\n 5 DISPLAY EMPLOYEE\n 6 EXIT')
    ch=int(input('Enter your choice: '))
    if ch==1:
        ems.addemployee()
    elif ch==2:
        ems.searchemployee()
    elif ch==3:
        ems.modifyemployee()
    elif ch==4:
        ems.deleteemployee()
    elif ch==5:
        ems.displayemployee()
    elif ch==6:
        break
    else:
        print('INVALID CHOICE')


