print("===== Q.1 =====")
'''
number = -1

if number < 0:
    raise ValueError("number must be positive")
'''
print("===== Q.2 =====")
'''
def Check_even(n):
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n % 2 != 0:
        raise ValueError("Number must be even")

    return n

try:
    num = int(input("Enter a number: "))
    Check_even(num)
    print("Number is even")

except TypeError as e:
    print("TypeError:", e)

except ValueError as e:
    print("ValueError:", e)
'''
print("===== Q.3 =====")
'''
num = int(input("Enter a age: "))

assert num> 18 , "AssertionError"

'''

print("===== Q.4 =====")
'''
def check_palindrome(s):
    assert s != "", "String must not be empty"
    print("String is not empty")
    
text = input("Enter a string: ")

check_palindrome(text)

'''
print("===== Q.5 =====")
'''
class InsufficientBalanceError(Exception):
    """ Raised When a withdrawal excced the available balance."""
    pass

class BankAccount:
    
    def __init__(self , balance = 0):
        self.balance = balance

    def withdraw(self , amount):
        assert amount > 0 , "Withdrwal amount must be positive."
        
        if amount > self.balance:
            raise InsufficientBalanceError(f"cannot withdraw {amount} balance is only {self.balance}")
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(1000)
    account.withdraw(100)
except InsufficientBalanceError as e :
    print(f"Transaction failed: {e}")
'''
print("===== Q.6 =====")
'''
class InvalidEmailError(Exception):
    """ Raised when a @ and .com and .org not use"""
    pass

def validate_email(email):
    

    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailError("Invalid email address")

    print("Valid email enter")

email = input("Enter Your Email: ")
try:
    validate_email(email)

except InvalidEmailError as e:
    print("Error:", e)

'''

print("===== Q.7 =====")
'''
class InvalidGradeError(Exception):
    pass

grade = input("Enter your grade: ")

try:
    assert grade != "", "Grade cannot be empty"

    grade = float(grade)

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")

    if grade < 40:
        raise InvalidGradeError("Grade is below 40. Student has failed.")

    print("Grade is valid. Student has passed.")

except AssertionError as e:
    print("AssertionError:", e)

except ValueError as e:
    print("ValueError:", e)

except InvalidGradeError as e:
    print("InvalidGradeError:", e)
'''
print("===== Q.8 =====")

class HighTemperatureError(Exception):
    pass


def temperature_conversion(temp):

    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number")

    assert -273 <= temp <= 10000, "Temperature must be between -273°C and 10,000°C"

    if temp > 1000:
        raise HighTemperatureError(
            "Temperature exceeds 1,000°C and may be unrealistic for common applications"
        )

    print("Temperature is valid:", temp, "°C")


try:
    value = input("Enter temperature: ")

    try:
        value = float(value)
    except ValueError:
        raise TypeError("Temperature must be a number")

    temperature_conversion(value)

except TypeError as e:
    print("TypeError:", e)

except AssertionError as e:
    print("AssertionError:", e)

except HighTemperatureError as e:
    print("HighTemperatureError:", e)



















  




































