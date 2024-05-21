class Authentication:
    def auth(self,u_name,pass_,bal):
        self.bal=bal
        if u_name==pass_:
            choice=int(input("select 1 for withdrawl\nselect 2 for deposit\n select 3 for check balance"))
            match choice:
                case 1:
                    with_dr=int(input("enter the amount to be withdraw:"))
                    obj.withdraw(with_dr,self.bal)
                case 2:
                    depo=int(input("enter the amount to be withdraw:"))
                    obj.deposit(depo,self.bal)
                case 3:
                    obj.display(self.bal)
        
    def withdraw(self,with_dr,bal):
        
u_name=input("enter the username:")
pass_=input("enter the password:")
bal=1000
obj=Authentication()
obj.auth(u_name,pass_,bal)
        
    
        
