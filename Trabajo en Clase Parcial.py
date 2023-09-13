user_pass = ["Mushroom Peter", "pepe1234"]
#Valida el usuario
while True :
    user = input("User: ")
    password = input("Password: ")
    if(user == user_pass[0] and password == user_pass[1]):
        print("Correct")
        break
    else:
        print("Invalid user or password, please try again")

bank_account = 0.0
a_bank_account = 0.0
movements = []

#Recibe un monto, comprueba 
def deposit(b_account, mov):
    while True:
        dep = float(input("Please enter the amount to deposit: "))
        if dep > 0:
            b_account += dep
            print("Your account D: ", b_account)
            mov.append(f"D ${dep}")
            return b_account
        else:
            print("Enter a valid amount")

def withdraw(b_account, mov):
    while True:
        wd = float(input("Please enter the amount to withdraw: "))
        if wd <= b_account:
            b_account -= wd
            print("Your account WD: ", b_account)
            mov.append(f"W ${wd}")
            return b_account
        else:
            print("Enter a valid amount")

def transfer(b_account ,a_b_account, mov):
    while True:
        tf = float(input("Please enter the amount to tf: "))
        if tf <= b_account:
            b_account -= tf
            a_b_account += tf
            print("Your account TF: ", b_account)
            print("Another account TF: ", a_b_account)
            mov.append(f"TF ${tf}")
            return b_account, a_b_account
        else:
            print("Enter a valid amount")


def b_movements(mov):
    for m in mov:
        print(m, end="\n")



while True:
    menu = int(input("\t\t---Menu---\n1) Deposit\n2) Withdraw\n3) Transfer\n4) Movements\n5) Exit\n: "))

    if menu == 1:
        bank_account = deposit(bank_account, movements)
    elif menu == 2:
        bank_account = withdraw(bank_account, movements)
    elif menu == 3:
        bank_account, a_bank_account = transfer(bank_account,a_bank_account, movements)
    elif menu == 4:
        b_movements(movements)
    elif menu == 5:
        print("Thank you for using our service")
        break
    elif menu < 1 or menu > 5:
        print("Invalid number, try again")