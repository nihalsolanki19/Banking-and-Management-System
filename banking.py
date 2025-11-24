import json
import os
import random

# loading acc data from file (if the file is not there I make new one)
def load_data():
    if not os.path.exists("bank_data.json"):
        return {"accs": []}
    f = open("bank_data.json", "r")
    dt = json.load(f)
    f.close()
    return dt


# saving the updated acc data
def save_data(d):
    with open("bank_data.json", "w") as f:
        json.dump(d, f, indent = 3)



# making account 
def newAcc(d):
    name = input("Name: ")
    depo = float(input("Initial deposit: "))

    # random acc generator (simple)
    no = random.randint(10000,99999)

    acc = {
        "no": no,
        "name": name,
        "bal": depo
    }

    d["accs"].append(acc)
    save_data(d)
    print("Account made! Your number =", no)



# deposit amt 
def deposit(d):
    accNo = int(input("Acc no: "))
    found = False

    for a in d["accs"]:
        if a["no"] == accNo:
            amt = float(input("Deposit amount: "))
            a["bal"] = a["bal"] + amt      # updated
            found = True
            save_data(d)
            print("Money added.")
            break
    
    if not found:
        print("No such acc.")



# withdrawing 
def withdraw(d):
    accNo = int(input("Enter acc no: "))
    ok = False

    for a in d["accs"]:
        if a["no"] == accNo:
            amt = float(input("Withdraw amt: "))
            if amt <= a["bal"]:
                a["bal"] -= amt
                print("Done.")
                save_data(d)
            else:
                print("Not enough bal.")
            ok = True
            break

    if ok == False:
        print("No acc found.")



# checking bal 
def check(d):
    accNo = int(input("Acc number: "))
    for a in d["accs"]:
        if a["no"] == accNo:
            print("Your balance is:", a["bal"])
            return
    print("Acc not found")



# main menu
def main():
    data = load_data()

    while True:
        print("\n----- BANK MENU -----")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance")
        print("5. Exit")
        
        ch = input("Your choice: ")

        if ch == "1":
            newAcc(data)
        elif ch == "2":
            deposit(data)
        elif ch == "3":
            withdraw(data)
        elif ch == "4":
            check(data)
        elif ch == "5":
            break
        else:
            print("Invalid choice...")

main()