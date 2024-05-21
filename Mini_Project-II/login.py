'''import csv
def Register(self,username,password,name,phoneno,city):
    self.u_name=username
    self.u_pass=password
    self.name=name
    self.u_phno=phoneno
    self.city=city
    with open("details.csv","a",newline="") as file:
        store=csv.writer(file)
        store.writerrow([self.u_name,self.u_pass,self.name,self.u_phno,self.city])
def authenticate_user(username, password):
    with open("details.csv","r",newline="") as f:
        read=csv.DictWriter(f)
        for row in read:
            if row['username']==username and row['pass']==password:
                return True
'''
import csv
class Hello:

    def register(self, username, password, name, phoneno, u_city):
        self.username=username
        self.password=password
        self.name=name
        self.phoneno=phoneno
        self.u_city=u_city
        
        with open("details.csv", "a", newline="") as file:
            store = csv.writer(file)
            store.writerow(["username","password","name","user phoneno","user city"])
            
            store.writerow([self.username,self.password,self.name,self.phoneno,self.u_city])
            print("Registration successful")
    def authenticate_user(self,u_name,u_pass):
      
        with open("details.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if (row['username'] ==u_name and row['password'] ==u_pass):
                    return True
        return False


    


