
def display(rem_amo):
      print("The current balance in the ATM:",rem_amo) 
def check_balance(bank):
   
      print("The current balance in your bank account:",bank) 

def withdraw(amo,bank):
      if amo>bank:
            print("Your have insufficient amount to be withdraw")
      else:
            bank-=amo
            print("The amount after withdrawn:",bank)
    #return True

def deposit(bank,amo):
    bank+=amo
    print("The amount after deposited:",rem_amo)

"""def cardtypes():
        self.cardtype=input("Enter the card type you have('1.Rupay','2.Visa','3.Mastercard'):")
        if self.cardtype=="1" or self.cardtype=="Rupay":
            return obj.auth()
        elif self.cardtype=="2" or self.cardtype=="Visa" :
            return obj.auth()
        elif self.cardtype=="3" or self.cardtype=="Mastercard":
            return obj.auth()
        else:
            print("Card types not found")
"""
