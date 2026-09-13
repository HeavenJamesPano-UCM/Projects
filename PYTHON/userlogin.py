"""
user login
login information
-------------------
email : alpha@uc.com
password : hello123
"""
from os import system
from pwinput import *
import slists


email:str=None
password:str=None

def loginform(formname:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global email,password
            system("cls")
            print(formname.upper().center(21,"-") )
            email = input("E-MAIL :")
            password = pwinput("PASSWORD :")
            return func()
        return wrapper
    return decorator
    
@loginform("user login")
def validateuser()->bool:
    ok:bool = True if email.lower()=="alpha@uc.com" and password.lower()=="hello123" else False
    return ok

def main()->None:
    system("cls")
    ok:bool = validateuser()
    if ok:
        print("LOGIN SUCCESS")
        input("\nPress any key to continue...")
        slists.main()
  
    else:
        print("Invalid User") 
if __name__=="__main__":
    main() 