# Example Program 2
# This program will simulate a bank. You will be able to withdraw and deposit
# money


def checkValid(bank: list) -> list:
    # This function will return user info if user enters valid
    # username and password
    userCount = 0
    userInfo = []
    while userCount != 3:
        user = input("Input your username: ")
        pin = input("Input your PIN: ")
        for person in bank:
            dataName = person.get("UserName") # database username
            dataPin = person.get("PIN") # database Pin
            if dataName == user and dataPin == pin:
                checkBal = person.get("CheckingBalance")
                saveBal = person.get("SavingsBalance")
                userInfo.extend([dataName, dataPin, int(checkBal), int(saveBal)])
                return userInfo
        print("Incorrect Pin; Please try again.")
        userCount += 1
    return userInfo


def selectAcc() -> int:
    # return 1 for checking
    # return 2 for savings
    while True:
        choice = input("(s)avings or (c)hecking account? ")
        if choice == 's':
            return 2
        elif choice == 'c':
            return 1
        else:
            print("Please enter s or c.")


def makeDeposit(info: list) -> list:
    # allows user to make deposits in accounts
    accType = selectAcc()
    while True:
        userChoice = int(input("How much would you like to deposit? "))
        if userChoice <= 0:
            print("You must deposit more than 0 dollars.")
        else:
            if accType == 1:
                info[2] += userChoice
                return info
            else:
                info[3] += userChoice
                return info


def makeWithdrawal(info: list) -> list:
    # allows user to withdraw money from accounts
    accType = selectAcc()
    while True:
        userChoice = int(input("How much would you like to withdraw? "))
        if userChoice <= 0:
            print("You must withdraw more than 0 dollars.")
        else:
            # As long as user inputs an amount <= amount in account
            # Having 0 balance is legal
            if accType == 1 and userChoice <= info[2]:
                info[2] -= userChoice
                return info
            elif accType == 2 and userChoice <= info[3]:
                info[3] -= userChoice
                return info
            else:
                print("You must withdraw within your account balance.")


def printReceipt(userFinal: list) -> None:
    # Reports the final account balance in a text file
    receipt = open("Receipt.txt", "w")
    line = "Thank you for stopping by today! \n"
    line += "Your current checking account balance: " + str(userFinal[2])
    line += "\n Your current savings account balance: " + str(userFinal[3])
    receipt.write(line)
    receipt.close()
    return


def bankProcess(userInfo: list) -> None:
    curList = userInfo
    while True:
        userChoice = input("Would you like to (d)eposit, (w)ithdraw, or (q)uit? ")
        if userChoice == 'q':
            # user wants to quit
            printReceipt(curList)
            print('quitting')
            return
        elif userChoice == 'd':
            # user wants to deposit
            makeDeposit(curList)
        elif userChoice == 'w':
            # user wants to withdraw
            makeWithdrawal(curList)
        else:
            print("Enter a valid choice.")


def main() -> None:
    bank = [
    {'UserName':'Rich', 'PIN':'3867', 'CheckingBalance':'6598', 'SavingsBalance':'982374'},
    {'UserName':'Steve', 'PIN':'1234', 'CheckingBalance':'2354', 'SavingsBalance':'29837'},
    {'UserName':'Michael', 'PIN':'2459', 'CheckingBalance':'3647', 'SavingsBalance':'345234'},
    {'UserName':'Tina', 'PIN':'5093', 'CheckingBalance':'6454', 'SavingsBalance':'123423'},
    {'UserName':'Joe', 'PIN':'9876', 'CheckingBalance':'3452', 'SavingsBalance':'2456252'},
    ]
    user = checkValid(bank)
    if not user:
        # list is empty -> user not found from database
        print("You exceeded the number of login re-tries.")
    else:
        bankProcess(user)


if __name__ == "__main__":
    main()

