class ATM:
    def __init__(self, name, cardNo, pinNo, acBalance, taxDue, loanDue, loanNeeded):
        self.name = name
        self.cardNo = cardNo
        self.pinNo = pinNo
        self.acBalance = acBalance
        self.cashToWithdraw = 0
        self.loanDue = loanDue
        self.loanNeeded = loanNeeded
        self.loanAmt = 0
        self.taxDue = taxDue
        self.pinInput = 0

    def withdrawCash(self):
        self.pinInput = int(input("Enter your pin: "))
        if self.pinInput == self.pinNo:
            self.cashToWithdraw = int(input("Enter the amount you wish to withdraw: "))
            if self.cashToWithdraw <= self.acBalance:
                print("Rs. ", self.cashToWithdraw, " have been successfully credited from your account. Please collect your cash")
                self.acBalance -= self.cashToWithdraw
            elif self.cashToWithdraw > self.acBalance:
                print("Not enough balance in account!")
        else:
            print("Invalid Pin No.")
            

    def balanceEnquiry(self):
        self.pinInput = int(input("Enter your pin: "))
        if self.pinInput == self.pinNo:
            print("Name of the Card-holder: ", self.name)
            print("Card No.: ", str(self.cardNo))
            print("Balance in account: Rs. ", str(self.acBalance))
        else:
            print("Invalid Pin No.")

    def getLoan(self):
        self.pinInput = int(input("Enter your pin: "))
        if self.pinInput == self.pinNo:
            if self.loanDue > 0:
                print("Please repay your previous dues")
            elif self.loanDue == 0:
                self.loanNeeded = True
                self.loanAmt = int(input("Please enter the amount you wish to borrow: "))
                self.acBalance += self.loanAmt
                self.loanDue = self.loanAmt
                print("Amount successfully credited in your bank account!")
        else:
            print("Invalid Pin No.")
    
    def repayLoan(self):
        self.pinInput = int(input("Enter your pin: "))
        if self.pinInput == self.pinNo:
            if self.acBalance >= self.loanDue:
                self.acBalance -= self.loanDue
                self.loanDue = 0
                print("Loan repaid")
            elif self.acBalance < self.loanDue:
                print("Please deposit sufficient money in your account")
        else:
            print("Invalid Pin No.")

    def payTax(self):
        self.pinInput = int(input("Enter your pin: "))
        if self.pinInput == self.pinNo:
            if self.taxDue == 0:
                print("No pending dues!")
            elif self.taxDue > 0:
                if self.acBalance >= self.taxDue:
                    self.acBalance -= self.taxDue
                    print("Your tax has been paid!")
                elif self.acBalance < self.taxDue:
                    print("Please deposit sufficient money in your account")
        else:
            print("Invalid Pin No.")
    
cardHolder1 = ATM("Gargi Chaturvedi", 1234567890, 4853, 10000, 1000, 0, False)
cardHolder2 = ATM("Rakhi Chaturvedi", 9876543201, 9786, 50000, 5000, 3000, False)

inputName = input("Enter your name: ");

if inputName == cardHolder1.name:
    choice1 = int(input("Enter your choice corresponding to the sr. no:\n1. Withdraw Cash\n2. Balance Enquiry\n3. Get Loan\n4. Repay Loan\n5. Pay Taxes\n"))
    if choice1 == 1:
        cardHolder1.withdrawCash()
    elif choice1 == 2:
        cardHolder1.balanceEnquiry()
    elif choice1 == 3:
        cardHolder1.getLoan()
    elif choice1 == 4:
        cardHolder1.repayLoan()
    elif choice1 == 5:
        cardHolder1.payTax()
    else:
        print("Invalid Choice")

elif inputName == cardHolder2.name:
    choice2 = int(input("Enter your choice corresponding to the sr. no:\n1. Withdraw Cash\n2. Balance Enquiry\n3. Get Loan\n4. Repay Loan\n5. Pay Taxes"))
    if choice2 == 1:
        cardHolder2.withdrawCash()
    elif choice2 == 2:
        cardHolder2.balanceEnquiry()
    elif choice2 == 3:
        cardHolder2.getLoan()
    elif choice2 == 4:
        cardHolder2.repayLoan()
    elif choice2 == 5:
        cardHolder2.payTax()
    else:
        print("Invalid Choice")

else:
    print("User not found!")