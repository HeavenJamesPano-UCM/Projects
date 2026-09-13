'''
student list management
'''
from os import system
students:list = [
    {'idno':'1000','name':'alpha','course':'bsit','level':'2',},
    {'idno':'1001','name':'bravo','course':'bscs','level':'1',},
    {'idno':'1002','name':'charlie','course':'bst','level':'3',},
    {'idno':'1003','name':'delta','course':'bshm','level':'2',},
]
idno:str = None
name:str = None
course:str = None
level:str = None

def studentidno(formname:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global idno
            system("cls")
            print(formname.upper().center(21,"-"))
            idno    = input ("IDNO      :")
            print("-"*21)
            func()
        return wrapper
    return decorator

def studentinput(formname:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global idno,name,course,level
            system("cls")
            print(formname.upper().center(21,"-"))
            idno    = input ("IDNO      :")
            name    = input ("NAME      :")
            course  = input ("COURSE    :")
            level   = input ("LEVEL     :")
            print("-"*21)
            func()
        return wrapper
    return decorator
    
@studentinput("Add student")
def add()->None:
    
    if not idno or not name or not course or not level:
        print("please fill the blanks")
        return
    
    student:dict = {
        'idno':idno,
        'name':name,
        'course':course,
        'level':level,
    }
    students.append(student)
    print("New Student Added")
    
@studentidno("Find student")
def find()->None:
    if len(students)>0:
        for student in students:
            if idno == student['idno']:
                print(student)
    else:
        print("List is Empty !")

@studentidno("Delete student")
def delete()->None:
    index:int = 99999
    if len(students)>0:
        for student in students:
            if idno == student['idno']:
                index = students.index(student)
                print(f"Student Found: {student}")
                opt:str = input("Do you really want to delete this (Y/N)?")
                if opt.upper()=='Y':
                    students.pop(index)
                    print("Student Deleted !!!")
                else:
                    print("Student NOT Deleted !!!")
    else:
        print("List is Empty !")
    
@studentidno("Update student")  
def update()->None:
    
    
    index:int = 99999
    if len(students)>0:
        for student in students:
            if idno == student['idno']:
                index = students.index(student)
                print(f"Student Found: {student}")
                opt:str = input("Do you really want to update this (Y/N)?")
                if opt.upper()=='Y':
                    new_idno=input("ENTER IDNO     :")
                    new_name=input("ENTER NAME     :")
                    new_course=input("ENTER COURSE   :")
                    new_level=input("ENTER LEVEL    :")
                    if not new_idno or not new_name or not new_course or not new_level:
                        print("please fill the blanks")
                    else:
                        newstudent :dict ={
                            'idno':new_idno,
                            'name':new_name,
                            'course':new_course,
                            'level':new_level,
                        }
                        students[index] = newstudent
                        print("Student Updated !!!")
                else:
                    print("Student NOT Updated !!!")
    else:
        print("List is Empty !")


def displayall()->None:
    system("cls")
    print("-- STUDENT LIST ",end="")
    print("-"*64)
    for student in students:
        print(f"{student['idno']}\t\t{student['name'].upper()}\t\t{student['course'].upper()}\t\t{student['level']}")
    print("-"*80)

def menu()->None:
    system("cls")
    print(" MAIN MENU ".center(21,"-"))
    print("1. ADD STUDENT ")
    print("2. FIND STUDENT ")
    print("3. DELETE STUDENT ")
    print("4. UPDATE STUDENT ")
    print("5. DISPLAY ALL STUDENTS ")
    print("0. QUIT/EXIT ")
    print("-"*21)
    
def main()->None:
    option:int = 9999
    while option!=0:
        menu()
        try:
            option=int(input("Enter Option(0...5) "))
            if   option == 1: add()
            elif option == 2: find()
            elif option == 3: delete()
            elif option == 4: update()
            elif option == 5: displayall()
            elif option == 0: print("program ends....")
            
        except ValueError as e:
            print(f"Invalid input :{e}")
        input("\nPress any key to continue...")
if __name__=="__main__":
    main()