class CarShowRoom:
    def __init__(self,name):
        self.name=name
        self.insurance=(5/100)
        self.cgst=(3/100)
        self.sgst=(2/100)
        if name=="toyota":
            print("Welcome to Toyoto Family")
            self.model=self.carmod(name)
            self.vari=self.carvar(mod,name,var)
            self.display(name,mod,self.vari)
        elif name=="mahindra":
            print("Welcome to mahindra Family")
            self.model=self.carmod(name)
            self.vari=self.carvar(mod,name,var)
            self.display(name,mod,self.vari)
        elif name=="mercedes":
            print("Welcome to mercedes Family")
            self.model=self.carmod(name)
            self.vari=self.carvar(mod,name,var)
            self.display(name,mod,self.vari)
        else:
            print("No such car company is present in our showroom please select a valid car company")

    def carmod(self,name):
        if name=="toyota":
            mod=input("select one from hycross and glanza:")
            if mod=="hycross" or mod=="glanza":
                var=input("select which variant you want {petrol,diesel}:")
                return self.carvar(mod,name,var)
            else:
                print("select appropriate options")
                
        elif name=="mahindra":
            mod=input("select one from thar and xuv700:")
            if mod=="thar" or mod=="xuv700":
                var=input("select which variant you want {petrol,diesel}:")
                return self.carvar(mod,name,var)
            else:
                print("select appropriate options")
        elif name=="mercedes":
            mod=input("select one from cqs and gls:")
            if mod=="cqs" or mod=="gls":
                var=input("select which variant you want {petrol,diesel}:")
                return self.carvar(mod,name,var)
            else:
                print("select appropriate options")
            
            
    def carvar(self,model,name,var):
        if model=="hycross" and name=="toyota"and var== "petrol":
            return var
        elif model=="hycross" and name=="toyota" and var== "diesel":
            return var
        elif model=="glanza" and name=="toyota" and var== "petrol":
            return var
        elif model=="glanza" and name=="toyota" and var== "diesel":
            return var
        elif model=="thar" and name=="mahindra" and var== "petrol":
            return var
        elif model=="thar" and name=="mahindra" and var== "diesel":
            return var
        elif model=="xuv700" and name=="mahindra" and var== "petrol":
            return var
        elif model=="xuv700" and name=="mahindra" and var== "diesel":
            return var
        elif model=="cqs" and name=="mercedes" and var=="petrol":
            return var
        elif model=="cqs" and name=="mercedes" and var=="diesel":
            return var
        elif model=="gls" and name=="mercedes" and var=="petrol":
            return var
        elif model=="gls" and name=="mercedes" and var=="diesel":
            return var
        else:
            print("select appropriate options")
    def display(self,model,name,var):
        if model=="hycross" and name=="toyota"and var== "petrol":
            exshow=2000000
            print("The ex-showroom prince of toyota's hycross model petrol varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of toyota's hycross model petrol varient is",onroad)
        elif model=="hycross" and name=="toyota" and var== "diesel":
            exshow=1977000
            print("The ex-showroom prince of toyota's hycross model diesel varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of toyota's hycross model diesel varient is",onroad)
        elif model=="glanza" and name=="toyota" and var== "petrol":
            exshow=1854000
            print("The ex-showroom prince of toyota's glanza model petrol varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of toyota's glanza model petrol varient is",onroad)
        elif model=="glanza" and name=="toyota" and var== "diesel":
            exshow=1800000
            print("The ex-showroom prince of toyota's glanza model diesel varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of toyota's glanza model diesel varient is",onroad)
        elif model=="thar" and name=="mahindra" and var== "petrol":
            exshow=1000000
            print("The ex-showroom prince of mahindra's thar model petrol varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mahindra's thar model petrol varient is",onroad)
        elif model=="thar" and name=="mahindra" and var== "diesel":
            exshow=981000
            print("The ex-showroom prince of mahindra's thar model diesel varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mahindra's thar model diesel varient is",onroad)
        elif model=="xuv700" and name=="mahindra" and var== "petrol":
            exshow=2000000
            print("The ex-showroom prince of mahindra's xuv700 model petrol varient is",exshow,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mahindra's xuv700 model petrol varient is",onroad)
        elif model=="xuv700" and name=="mahindra" and var== "diesel":
            exshow=1980000
            print("The ex-showroom prince of mahindra's xuv700 model diesel varient is",exshowroo,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mahindra's xuv700 model diesel varient is",onroad)
        elif model=="cqs" and name=="mercedes" and var=="petrol":
            exshow=15000000
            print("The ex-showroom prince of mercedes's cqs model petrol varient is",exshowroo,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mercedes's cqs model petrol varient is",onroad)
        elif model=="cqs" and name=="mercedes" and var=="diesel":
            exshow=14000000
            print("The ex-showroom prince of mercedes's cqs model diesel varient is",exshowroo,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mercedes's cqs model diesel varient is",onroad)
        elif model=="gls" and name=="mercedes" and var=="petrol":
            exshow=13000000
            print("The ex-showroom prince of mercedes's gls model petrol varient is",exshowroo,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mercedes's gls model petrol varient is",onroad)
        elif model=="gls" and name=="mercedes" and var=="diesel":
            exshow=12000000
            print("The ex-showroom prince of mercedes's gls model diesel varient is",exshowroo,)
            onroad=(exshow*insurance)+(exshow*sgst)+(exshow*cgst)
            print("The onroad prince of mercedes's gls model diesel varient is",onroad)
        
            
            
        
   
name=input("enter the car company you need select from these three{toyota,mahindra,mercedes}:")
obj=CarShowRoom(name)

