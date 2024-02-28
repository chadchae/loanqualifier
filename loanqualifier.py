# loanqualifier.py
# This program get input from user and determin accetance or rejection of a loan application

# Set minimum salary and year or work
MINSALARY = 40000
MINYEAR = 5
# Get input from user about salary and year
SALARY = float(input("Please enter your annual salary: "))
YEAR = int(input("Please enter your year of work: "))
# Determine whether the loan application is accepted or jected
if SALARY > MINSALARY and YEAR > MINYEAR:
    print("Congratulation, your application has accepted")
else:
    print("Sorry, your application has rejected")