# INFORMATİON ABOUT UNIVERSİTY STUDENTS

import json,os
class StudentInfo:
    def __init__(self,name,surname,uniName,department,grade,studentNumber):
        self.name=name
        self.surname=surname
        self.uniName=uniName
        self.department=department
        self.grade=grade
        self.studentNumber=studentNumber
class AllStudents:
    def __init__(self):
        self.students=[]
        self.loadtheStudentsBack()
        self.addtoFile()
    
    def addtoFile(self):
        list=[]
        for student in self.students:
            list.append(json.dumps(student.__dict__))
        with open('students.json','w',encoding='utf-8')as file:
            json.dump(list,file)

    def register(self,student:StudentInfo):
        self.students.append(student)
        self.addtoFile()
        print('Student registered')

    def loadtheStudentsBack(self):
        if os.path.exists('students.json'):
            with open('students.json','r',encoding='utf-8')as file:
                students=json.load(file)
                self.students
                iterator=iter(students)
                while True:
                    try:
                        student=next(iterator)
                        print(student)
                    except StopIteration:
                        break
repo=AllStudents()   
while True:
    print("Information About University Students".center(80,'*'))
    result=input('1-Register\n2-Add to File\n3-Load the Students Back\n4-Exit\n')
    if result=='1':
        name=input('Name:')
        surname=input('Surname:')
        uniName=input('University:')
        depatment=input('Department:')
        grade=int(input('Grade:'))
        studentNumber=int(input('Student Number:'))
        student=StudentInfo(name=name,surname=surname,uniName=uniName,department=depatment,grade=grade,studentNumber=studentNumber)
        repo.register(student)
        print(repo.students)
    elif result=='2':
        repo.addtoFile()
    elif result=='3':
        repo.loadtheStudentsBack()
    elif result=='4':
        break
    else:
        print('Wrong Answer')

        
    

    