from os import system
a:int = 0
b:int = 0

def mathinput(title:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global a, b
            system("cls")
            print(title.center(21,"-"))
            a=int(input("Enter First Value:"))
            b=int(input("Enter Second Value:"))
            func()
        return wrapper
    return decorator

@mathinput("ADDITION")
def add()->None:print(f"the sum of {a} and {b} is {a+b}")
@mathinput("SUBTRACTION")
def subtract()->None:print(f"the difference of {a} and {b} is {a-b}")
@mathinput("MULTIPLICATION")
def multiply()->None: print(f"the product of {a} and {b} is {a*b}")  
@mathinput("DIVISION")
def divide()->None:print(f"the qoutient of {a} and {b} is {a/b:.4f}")
def quitend()->None:print("Program ends....")


def menu()->None:
    system("cls")
    print("MAIN MENU".center(21,"-"))
    print("1. ADD ")
    print("2. MULTIPLY ")
    print("3. SUBTRACT  ")
    print("4. DIVIDE ")
    print("0. QUIT/END ")
    print("-"*21)
    
def main()->None:
    menuitems:dict = {
        1:add,
        2:multiply,
        3:subtract,
        4:divide,
        0:quitend
    }
      
    option:int = 999
    while option!=0:
        menu()
        try:
            option=int(input("Enter Option(0....5):"))
            menuitems.get(option)()
        except ValueError as e:
            print(f"Input Error : {e}")
        input("Press any key to continue...")
    
    
if __name__=="__main__":
    main()