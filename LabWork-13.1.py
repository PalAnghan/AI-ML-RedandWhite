print("===== Q.1 =====")
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

print("\n===== Q.2 =====")
import time

current_time = time.time()
print("Current time in seconds since the epoch:", current_time)

print("\n===== Q.3 =====")

import datetime

current_time = datetime.datetime.now()
date_format1 = current_time.strftime("%d-%m-%Y")
date_format2 = current_time.strftime("%m/%d/%Y")
time_format_12hr = current_time.strftime("%I:%M:%S %p")
time_format_24hr = current_time.strftime("%H:%M:%S")

print("Current date in YYYY-MM-DD format:", date_format1)
print("Current date in MM/DD/YYYY format:", date_format2)   
print("Current time in 12-hour format:", time_format_12hr)
print("Current time in 24-hour format:", time_format_24hr)

print("\n===== Q.4 =====")

date1 = datetime.datetime(2023, 1, 1)
date2 = datetime.datetime(2024, 1, 1)
difference = date2 - date1
print("Difference between", date2.date(), "and", date1.date(), "is:", difference.days, "days")

seven_days_later = now + datetime.timedelta(days=7)
print("Date after adding 7 days:", seven_days_later.date())

print("\n===== Q.5 =====")

import datetime
import time

date1 = "2024-01-01"
datetime_object = datetime.datetime.strptime(date1, "%Y-%m-%d")
print("String to datetime object:", datetime_object)

print("Current datetime object:", now)

datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
print("Datetime object to string:", datetime_string)

print("\n===== Q.6 =====")

import time

print("Measuring execution time of a function using time module")

def sample_function():
    total = 0
    for i in range(1, 10000000):
        total += i
    return total

start_time = time.time()
result = sample_function()
print("Result of the function:", result)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time of the function:", execution_time, "seconds")

print("\n===== Q.7 =====")
import datetime

utc_now = datetime.datetime.utcnow()
local_now = datetime.datetime.now()

print("Current UTC date and time:", utc_now)
print("Current local date and time:", local_now)

print("\n===== Q.8 =====")

import time

print("Stopwatch Simulation")
def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))

stopwatch()

print("\n===== Q.9 =====")

import datetime

def  number_second():
    num_of_seconds = int(input("Enter the number of seconds for countdown: "))
    while num_of_seconds > 0:
        print("Time remaining: {} seconds".format(num_of_seconds))
        time.sleep(1)
        num_of_seconds -= 1 

number_second()

print("\n===== Q.10 =====")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

print("\n===== Q.11 =====")

import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")
date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d")
print("The day of the week for", date_input, "is:", date_object.strftime("%A"))

print("\n===== Q.12 =====")
# writa a program that schedule a reminder at a specific time using the time.sleep() function.
import time

def schedule_reminder(reminder_time, message):
    current_time = time.time()
    reminder_timestamp = time.mktime(time.strptime(reminder_time, "%Y-%m-%d %H:%M:%S"))
    time_to_wait = reminder_timestamp - current_time

    if time_to_wait > 0:
        print("Reminder scheduled for", reminder_time)
        time.sleep(time_to_wait)
        print("Reminder:", message)
    else:
        print("The specified time is in the past. Please enter a future time.")

reminder_time = input("Enter the reminder time (YYYY-MM-DD HH:MM:SS): ")
message = input("Enter the reminder message: ")
schedule_reminder(reminder_time, message)

