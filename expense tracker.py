def load_expenses():
    expenses = []
    try:
        file = open("expenses.txt","r")
        for line in file:
            if line.strip() != "":
                parts = line.strip().split(",")
                name = parts[0]
                amount = float(parts[1])
                expenses.append([name,amount])
        file.close()
    except FileNotFoundError:
        print("file not found")
    return expenses

def save_expenses(expenses):
    try:
        file = open("expenses.txt","w")
        for item in expenses:
            file.write(item[0] + "," + str(item[1]) + "\n")
        file.close()
    except:
        print("file not found")

def add_expenses(expenses):
    name = input("enter expense name:")
    while True:
        amount_input = input("enter expense amount:")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("enter valid number")
    expenses.append([name,amount])
    save_expenses(expenses)
    print("expense added")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("no expenses found")
    else:
        total = 0
        print("expenses")
        for item in expenses:
            print(item[0], "-", item[1])
            total = total + item[1]
        print("Total spent:",total)

def delete_expense(expenses):
    name = input("enter name to delete:")
    flag = False
    for item in expenses:
        if item[0] == name:
            expenses.remove(item)
            flag = True
            print("expense deleted")
            break
    if flag == True:
        save_expenses(expenses)
    else:
        print("expense not found")


#main
expenses = load_expenses()
while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. Exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_expenses(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        delete_expense(expenses)
    elif choice == "4":
        print("goodbye")
        break
    else:
        print("invalid choice")






