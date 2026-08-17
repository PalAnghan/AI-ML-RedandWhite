from abc import ABC , abstractmethod
import math

print("=" * 40)
print("Q 1, Q 2:")
print("=" * 40)
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class IncompleteShape(Shape):
    
    def area(self):
        pass
    
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius 

try:
    s = Shape()
except TypeError as e:
    print("Shape Error:",e)

#try error
#err = IncompleteShape()
    
r = Rectangle(23,5)
print("Rectangle area: ",r.area())
print("Rectangle Perimeter: ",r.perimeter())

c = Circle(5)
print(f"Circle area: {c.area():.2f}")# 1 print to point value remove.
print(f"Circle area: ",round(c.area(),2))# 2 print to point value remove.
print(f"Circle area: {c.perimeter():.2f}")
'''
print("=" * 40)
print("Q 3:")
print("=" * 40)
'''
class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):
    #def __init__(self):

    def train(self):
        print("Linear Regression is training")

    def predict(self):
        print("Linear Regression is predicting")

class DecisionTreeModel(MLModel):
    #def __init__(self):

    def train(self):
        print("Decison Tree is training ")

    def predict(self):
        print("Decison Tree is predicting")

l1 = LinearRegressionModel()
l1.train()
l1.predict()

d1 = DecisionTreeModel()
d1.train()
d1.predict()
'''
print("=" * 40)
print("Q 4:")
print("=" * 40)
print("Bank Account Management System!")

class Account(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class BankAccount(Account):

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self):
        choice_dep = float(input("Enter a deposit amount: "))
        if choice_dep > 0:
            self.__balance += choice_dep
            print("Your Deposit Sucessfully!......")
        else:
            print("The amount must be Greater then 0....")

    def withdraw(self):
        choice_wit = float(input("Enter a withdraw amount: "))

        if choice_wit > 0 and choice_wit <= self.__balance:
            self.__balance -= choice_wit
            print("Your withdraw Sucessfully!......")
        else:
            print("The amount must be Greater then 0....")
            
class SavingsAccount(BankAccount):

    def __init__(self,account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self._BankAccount__balance += interest
        print("Interest Added Successfully!")


class CurrentAccount(BankAccount):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self):
        choice_wit = float(input("Enter a withdraw amount: "))
        overdraft_limit = 500

        if choice_wit > 0 and choice_wit <= self._BankAccount__balance + overdraft_limit:
            self._BankAccount__balance -= choice_wit
            print("Your withdraw Successfully.......")
        else:
            print("Withdraw limit exceeded.....")



# ==================== SAVINGS ACCOUNT TESTING ==================== #

saving = SavingsAccount(101, 10000, 5)

print("\nSavings Account Balance:", saving.get_balance())

saving.deposit()
saving.withdraw()
saving.add_interest()

print("Final Savings Balance:", saving.get_balance())


# ==================== CURRENT ACCOUNT TESTING ==================== #

print("\n" + "=" * 40)
print("Current Account Testing")
print("=" * 40)

current = CurrentAccount(102, 1000)

print("Current Account Balance:", current.get_balance())

current.deposit()
current.withdraw()

print("Final Current Account Balance:", current.get_balance())



















        

























