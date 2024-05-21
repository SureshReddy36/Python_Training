"""from login import *
class mainc:
    def main(self):
        print("enter 1 for registrations\nenter 2 for login\nenter 3 for orders\n")
        choose=int(input())
        if choose==1:
            u_name=input("enter username:")
            u_pass=input("enter password:")
            name=input("enter name:")
            u_phno=input("enter phone number:")
            u_city=input("enter city:")
            reg=Register(u_name,u_pass,name,u_phno,u_city)
            print("Registration successful")
obj=mainc()
obj.main()"""

from login import *
from products import *
class MainController:
    def main(self):
        print("Enter 1 for registration\nEnter 2 for login\nEnter 3 for orders:")
        choice = int(input())
        if choice == 1:
            self.u_name = input("Enter username: ")
            self.u_pass = input("Enter password: ")
            name = input("Enter name: ")
            u_phno = input("Enter phone number: ")
            u_city = input("Enter city: ")
            obj.register(self.u_name, self.u_pass, name, u_phno, u_city)
        elif choice ==2:
            self.u_name=input("enter username:")
            self.u_pass=input("enter password:")
            if obj.authenticate_user(self.u_name,self.u_pass):
                print("Login succesfully")
                
        elif choice==3:
            print("select 1 for electronics\nselect 2 for accessories\nselect 3 for Clothing:")
            select=int(input())
            if select==1:
                print("select 1 for mobile\nselect 2 for laptop\nselect 3 for watches:")
                sel=int(input())
                if sel==1:
                   obj2. mobile()
                elif sel==2:
                    obj2.laptop()
                elif sel == 3:
                    obj2.watch()
            elif select==2:
                print("select 1 for ear phones\nselect 2 for cases\nselect 3 for charger:")
                sel=int(input())
                if sel==1:
                   obj2. earphones()
                elif sel==2:
                    obj2.cases()
                elif sel == 3:
                    obj2.charger()
            elif select==3:
                print("select 1 for shirts\nselect 2 for pants\nselect 3 for trousers:")
                sel=int(input())
                if sel==1:
                   obj2. shirts()
                elif sel==2:
                    obj2.pants()
                elif sel == 3:
                    obj2.trousers()
            else:
                print("select valid product")

            
obj=Hello()
obj2=hi()
obj1= MainController()
obj1.main()


