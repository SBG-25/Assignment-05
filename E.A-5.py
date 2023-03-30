########## Problem-1

class point:
    def __init__(self,X,Y,Z):
        self.X=X
        self.Y=Y
        self.Z=Z
    def Sq_Sum(self):
        self.answer=(self.X**2)+(self.Y**2)+(self.Z**2)
        pass
    def Display(self):
        print(self.answer)
        
Sq=point(1,3,5)
Sq.Sq_Sum()
Sq.Display()

########## Problem-2

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)

obj = Calculator(10, 94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())

########## Problem-3

class Student:
  
    def setName(self,__name,StudentID):
        if StudentID=="SI123":
         self.__name=__name
        else:
           self.__name=StudentID
           print('Fallowing Student ID for student name is wrong')
    def getName(self):
        return self.__name
    
    def setRollno(self,__Rollno,StudentID):
        if StudentID=="SI123":
          self.__Rollno=__Rollno
        else:
           self.__Rollno=StudentID
           print('Fallowing Student ID for student rollnumber is wrong')
    def getRollno(self):
        return self.__Rollno
    
    
student=Student()
student.setName("SB","SI123")
student.setRollno("1234","SI123")
print(student.getName())
print(student.getRollno())

########## Problem-4

class Account:
    def __init__(self,title,balence):
        self.title=title
        self.balence=balence

class Saving(Account):
    def __init__(self,title,balence,interest):
        super().__init__(title,balence)
        self.interest=interest
Account=Saving("Ashish",5000,5)

print(f'Account Holder : {Account.title} \nAccount Ballence : {Account.balence} \nSavings Interest : {Account.interest}')

########## Problem-5

class Account:
    def __init__(self,title,balence):
        self.title=title
        self.balence=balence

    def deposit(self, deposit):
        self.balence=self.balence + deposit

    def withdraw(self,withdraw):
        if (self.balence < withdraw):
            print("Insufficiant Balence")
        else:
            self.balence=self.balence - withdraw
    def getbalence(self):
        return self.balence
    
class SevingAccount(Account):
    def __init__ (self,title,balence,interest):
        super().__init__(title,balence)
        self.interest=interest

    def intAmount(self):
        self.interestAmount=int(self.balence*self.interest/100)
        
        

    def display(self):
        print(f'Account Holder-{self.title} \nAccount balence-{self.balence} \nInterest Persent-{self.interest} \nInterest Amount-{self.interestAmount}')

Savings_Account=SevingAccount('Ashish',2000,5)
Savings_Account.deposit(200)
Savings_Account.withdraw(100)
Savings_Account.intAmount()
Savings_Account.display()
