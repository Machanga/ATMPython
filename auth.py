from datetime import datetime
import random

database = {}

# Initializing the system
def init():

    print('Welcome to bankPython')

    try:
        haveAccount = int(input('Do you have an account with us: 1 (Yes) 2 (No) \n'))
    except: 
        print("Oops! Only integers are allowed... Kindly try again.")
        haveAccount = int(input('Do you have an account with us: 1 (Yes) 2 (No) \n'))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

# Login functionality
def login():

    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()
    # sureHaveAccount = int(input('Are you sure you have an account? 1(Yes) 2(No) \n'))
    # if(sureHaveAccount == 1):
    #     login()
    # else:
    #     register()

# Account registration functionality
def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

# Bank operations
def bankOperation(user):
    print(datetime.now())
    print("Welcome %s %s " % ( user[0], user[1] ) )

    try:
        selectedOption = int(input("What would you like to do? (1) Withdrawal (2) Deposit (3) Complaint (4) Logout (5) Exit \n"))
    except:
        print("Oops! Only integers are allowed... Kindly try again.")
        selectedOption = int(input("What would you like to do? (1) Withdrawal (2) Deposit (3) Complaint (4) Logout (5) Exit \n"))

    if(selectedOption == 1):
        withdrawalOperation() 
    elif(selectedOption == 2):
        depositOperation()
    elif(selectedOption == 3):
        complaintOperation()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

# Withdrawal functionality
def withdrawalOperation():
    try:
        withdrawalAmount = int(input("How much would you like to withdraw? \n"))
    except:
        print("Oops! Only integers are allowed... Try again.")
        withdrawalAmount = int(input("How much would you like to withdraw? \n"))

    print("Take your Cash")
    exit()

# Deposit functionality
def depositOperation():
    try:
        deposit = int(input("How much would you like to deposit? \n"))
    except:
        print("Oops! Only integers are allowed... Try again.")
        deposit = int(input("How much would you like to deposit? \n"))

    currentBalance = random.randrange(1000, 10000000, 1000)
    balance = currentBalance + deposit
    print("Your balance is: {} ".format(balance))
    exit()

# Complaint functionality
def complaintOperation():
    complaint = input("What issue would you like to report? \n")
    print("Thank you for contacting us.")
    exit()

# Generating users account number
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

# logout functionality
def logout():
    login()

init()
 