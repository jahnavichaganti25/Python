bank_balance = 10000
def bank_account():
    print("Welcome")
    print("Enter your bank account details")
    Acc_no = input("Enter your account number: ")
    # Enter your account number: 229910100047965
    Ifsc_code = input("Enter your Ifsc code: ")
    # Enter your Ifsc code: U8IN0822990
    Branch_name = input("Enter your branch name: ")
    # Enter your branch name: Benz circle
    Cust_name = input("Enter the customer name: ")
    # Enter the customer name: Akshitha Sinha
    print("Your bank_account details:\nAccount_number: ", Acc_no, "\nIfsc_code: ", Ifsc_code, "\nBranch_name: ", Branch_name, "\nCustomer_name: ", Cust_name)
    print("Your bank balance:", bank_balance)
bank_account()
print("Enter your choice\n1. Credit\n2. Debit\n3. Check_Balance\n4. Exit\n")
h = int(input("Enter your choice: "))
# Enter your choice: 1
def credit():
    cr = int(input("Enter the amount to credit: "))
    # Enter the amount to credit: 2000
    print("After credit, your bank balance is: ", bank_balance + cr)
def debit():
    dr = int(input("Enter the amount to debit: "))
    print("After debit, your bank balance is: ", bank_balance - dr)
def check_balance():
    print("Your bank balance is:", bank_balance)
while (h == 1):
    credit()
    h = int(input("Enter your choice: "))
    # Enter your choice: 4
while (h == 2):
    debit()
    h = int(input("Enter your choice: "))
    if h == 1:
        credit()
        h = int(input("Enter your choice: "))
while (h == 3):
    check_balance()
    h = int(input("Enter your choice: "))
    if h == 1:
        credit()
        h = int(input("Enter your choice: "))
    elif h == 2:
        debit()
        h = int(input("Enter your choice: "))
while (h == 4):
    print("Thank you for visiting:)")
    break
