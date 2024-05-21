class Faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print("faculty_information:",self.f_name,self.department,self.f_id)
obj=Faculty("Shyam","Computer Science",101)
obj.print_info()
class Cse(Faculty):
    pass#no statement
obj=Cse("jyoti mam","Computer Science",102)
obj.print_info()

