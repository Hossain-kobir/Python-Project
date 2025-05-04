from abc import ABC,abstractmethod
import maskpass
class Account(ABC):
    accounts=[]
    Is_bankruft=False
    def __init__(self,name,password,type):
        self.name=name
        self.account_no=len(Account.accounts)+219000001280005291
        self.password=password
        self.balance=0
        self.type=type
        
        self.loan_limit=0

        Account.accounts.append(self)
        
        self.History=[]
    
    def deposite(self,amount):
         if amount > 0:
             self.balance+=amount
             print(f"\nBDT {amount} taka has been deposited Sucessfully account no: {self.account_no} Current Balance {self.balance}")
             self.History.append({
                "Type" : "Deposite",
                "Name" : self,
                "Amount":amount,
                "Account No":self,
                "Current Balance":self,
                
                
            })
         else:
             print("\nInvalid Amount Please Enter a valid amount")
    
    def withdraw(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance-=amount
            print(f"\nBDT {amount} taka has been withdrawn Sucessfully from account no: {self.account_no} Current Balance {self.balance}")

            self.History.append({
                "Type" : "Withdraw",
                "Name" : self,
                "Amount":amount,
                "Account No":self,
                "Current Balance":self,
                
                
            })
        else:
            print("\nInvalid amount please enter a valid amount")
    
    # opereator Overloading
    def Change_account_informaion(self,*args):
        prev_name=self.name
        prev_pass=self.password
        self.name=args[0]
        print(f"\nYour previous name was {prev_name} to update {self.name} Sucessfully")
        if len(args)>1:
            self.password=args[1]
            print(f"\nYour previous name was {prev_name} to {self.name} \n And your previous password was {prev_pass} to {self.password} update sucessfully")
    
    @abstractmethod
    def Show_info(self):
        pass
    
    @property
    def check_available_balance(self):
        return self.balance
    
    def Balance_tansfer(self):
        
        if self.Is_bankruft == False :
            try:
                num = int(input("\nEnter Account Number : "))
            except ValueError:
                print("\nInvalid input Please enter a number.")
                return

            nam=input("\nEnter Account Name : ")
            
            for account in Account.accounts:
                if account.account_no == num and account.name.lower() == nam.lower():
                    amount=int(input("\nEnter amount : "))
                    self.withdraw(amount)
                    print(f"\n{self.name}You have sucessfully transfer balance to \naccount name {account.name}\naccount no:{account.account_no}\n")
                    #self.name // transfer amount to account account.account_no
                    # name // account // to anotheer account number // account name
                    # self.History.append((self.name,amount,account))
                    self.History.append({
                        "Type"  :"Balance Transfer",
                        "sender": self.name,
                        "amount": amount,
                        "receiver": account,
                    })
                    account.deposite(amount)
                
                else:
                    print("\nAccount does not exist")
    
    def Transctions_History(self):
        # for hist in self.History:
           
        #     sender = hist[0]
        #     amount = hist[1]
        #     receiver_account = hist[2]  # this is the full account object!

        #     print(f"From: {sender}")
        #     print(f"Amount: ${amount}")
        #     print(f"To: {receiver_account.name} (Account No: {receiver_account.account_no})")

        # Transctions History Using Dictonary
        # for record in self.History:
        #     for key in record:
        #         if key == "timestamp":
        #             continue  # skip printing timestamp
        #         elif key == "receiver":
        #             receiver = record[key]
        #             print(f"{key.capitalize()}: {receiver.name} (Acc: {receiver.account_no})", end=" | ")
        #         else:
        #             print(f"{key.capitalize()}: {record[key]}", end=" | ")
        #     print()


        for str in self.History:
            if str['Type']=="Deposite":
                print(f"{self.name} Deposite {amount} to {self.account_no} Balance {self.balance}")
                
            elif str['Type']=="Withdraw":
                print(f"{self.name} withdraw {amount} from {self.account_no} Balance {self.balance}")
            
                
            elif str['Type']=="Balance Transfer":
                    print(f"{self.name} have been transfer {amount} Taka to {str['receiver'].account_no} Name : {str['receiver'].name} ")
            
            elif str['Type']=="Loan History":
                print(f"je loan nicce {self.name} tar account no {self.account_no} joto taka nilo eta get chara {str['loan_amount']}, eta get er {str.get('loan_amount',0)}")  
    
    def Take_Loan(self):
        
        try:
            loan_amount=int(input("\nPlease enter your loan amount : "))
        except ValueError:
            print("\nInvalid input please enter digit : ")
        Total_vault_balance=0
        for acc in self.accounts:
            Total_vault_balance+=acc.balance

        if 2 == self.loan_limit :
            print("\nSorry your Loan limit excedded")
        
        else:
            if Total_vault_balance-loan_amount >= loan_amount:
                Total_vault_balance-=loan_amount
                print(f"\n{self.name} You have got a loan BDT {loan_amount} from bank and deposite sucessfully to your account {self.name} no {self.account_no}")
                self.deposite(loan_amount)
                self.History.append({
                    "Type":"Loan History",
                    "Loan_reciver":self,
                    "loan_amount":loan_amount
                })
                self.loan_limit+=1
            else:
                print("\nYou have exceeded your limit")
    
        
class Savings_accounts(Account):
    def __init__(self, name,  password, irate):
        super().__init__(name,  password,"Savings")
        self.Interest_rate=irate
    
    def Show_info(self):
        print(f"\nInfos Of accounts {self.name} \n")
        print(f"Account number {self.account_no}")
        print(f"Account type {self.type}")
        print(f"Account balance BDT {self.balance} taka\n")
    
    def Apply_Interest(self):
        ir=self.balance*(self.Interest_rate/100)
        print("\nApply Interest Sucessfully")
        self.deposite(ir)

class Special_account(Account):
    def __init__(self, name,  password,limit):
        super().__init__(name,  password, "Current")
        self.limit=limit
    
    def Show_info(self):
        print(f"\nInfos Of Accounts {self.name} \n")
        print(f"Account Number {self.account_no}")
        print(f"Account Type {self.type}")
        print(f"Account Balance {self.balance} taka\n")
    
    #Method Overrideing
    def withdraw(self, amount):
        if amount > 0 and  (self.balance-amount)>=self.limit:
            self.balance-=amount
            print(f"\nBDT {amount} Taka Withdraw Sucessfully from account no {self.account_no}\naccount holder name {self.name}")
        
        else:
            print("\nInvalid Amount")

    # Main Function
    
currentuser=None

# currentuser=Special_account("kobir",234,123)
while (True):
        if currentuser == None:
            print("\nNo Loggen User")
            ch=input("\nLogin Or Register (L/R) ==:")

            if ch.lower() == "R".lower():
                # currentuser=Savings_accounts('hossain',123,10)
                nam=input("\nPlease Enter Your Name : ")
                # num=int(input("\nPlease Enter Your Account Numer : "))
                pas=maskpass.askpass("Please Enter Your Password : ",mask="*")

                type=input("\nPlease Enter Your account type savings or current Press:(SV/CR) : ")
                if type.lower() == "SV".lower():
                    ir=int(input("\nPlease Enter Your interest rate : "))
                    if ir <= 10:
                        
                        currentuser=Savings_accounts(nam,pas,ir)
                        
                    else:
                        print("\nInvalid Interest Rate")
        
                elif type.lower() == "CR".lower():
                    lmit=int(input("\nPlease Enter Your Special Limit : "))
                    if lmit <= 1000:
                        currentuser=Special_account(nam,pas,lmit)

                    else:
                        print("\nyour special amount limit exceeded")
                
                else:print("\nInvalid Input")
            
            elif ch.lower() == "L".lower():
                num=int(input("\nPlease Enter Your Account Numer : "))
                pas=input("\nPlease Enter Your Password : ")
                
                for account in Account.accounts:
                    if account.account_no == num and account.password == pas:
                        currentuser=account
                        break
                    
                    else:
                        print("\nPlease Enter a valid information")
        
        else:
            print(f"\nWelcome {currentuser.name}")
            if currentuser.type == "Savings" :
                print("\nShow Info Press 1")       
                print("Deposite Balance Press 2")       
                print("Withdraw Balance Press 3")       
                print("Change Account Information Press 4")     
                print("Apply Interest Press 5")  
                print("Check Available Balance 6")  
                print("Check Transctions History 7")  
                print("Balance Transfer Another Accounts 8") 
                print("Take Loan From Bank Account 9") 
                
                
                print("\nLogout Press 10")
                
                op=int(input("\nPlease Enter Your Choice : "))
                
                if op == 1:
                    currentuser.Show_info()
                
                elif op == 2:
                    amount=int(input("\nEnter Deposite Amount : "))
                    currentuser.deposite(amount)
                
                elif op == 3:
                    amount=int(input("\nEnter Amount : "))
                    currentuser.withdraw(amount)
                
                elif op == 4:
                        y=input("\nUpdate your information Press Yes or cancel Press anything ")

                        if y=="Yes":
                            print("\nUpdate Name press 1 : ")
                            print("\nUpdate Name and Password press 2 : ")
                            valu=int(input("\nEnter Input-->"))
                            if valu == 1:
                                name=input("\nPlease Enter Your Valid Name : ")
                                currentuser.Change_account_informaion(name)
                            elif valu == 2:
                                name=input("\nPlease Enter Your Valid Name : ")
                                password=maskpass.askpass(mask="#")
                                currentuser.Change_account_informaion(name,password)
                        
                        elif y == "cancel":
                            continue
                        
                        else:
                            print("\nCancel Sucessfully")
                           

                        

                    
                
                elif op == 5:
                    currentuser.Apply_Interest()
                
                elif op == 6:
                    currentuser.check_available_balance()
                
                elif op == 7:
                    currentuser.Transctions_History()
                    
                elif op == 8:
                    currentuser.Balance_tansfer()
                
                elif op == 9:
                    currentuser.Take_Loan()
                
                elif op == 10: 
                    currentuser = None
                
                else:
                    print("\nInvalid Input")
            else:
                print("\nShow Info Press 1")       
                print("Deposite Balance Press 2")       
                print("Withdraw Balance Press 3")       
                print("Change Account Information Press 4")     
                print("Check Available Balance 5")  
                print("Check Transctions History 6")  
                print("Balance Transfer Another Accounts 7") 
                print("Take Loan From Bank Account 8") 
                
                print("\nLogout Press 9")
                op=int(input("\nPlease Enter Your Choice :"))
                
                if op == 1:
                    currentuser.Show_info()
                
                elif op == 2:
                    amount=int(input("\nEnter Deposite Amount : "))
                    currentuser.deposite(amount)
                
                elif op == 3:
                    amount=int(input("\nEnter Amount : "))
                    currentuser.withdraw(amount)
                
                elif op == 4:
                    # change information implemented need
                    pass
                
                
                elif op == 6:
                    currentuser.Transctions_History()
                
                elif op == 7:
                    currentuser.Balance_tansfer()
                    
                elif op == 8:
                    currentuser.Take_Loan()
                
                elif op == 9:
                    currentuser = None     
                
                else:
                    print("\nInvalid Input")
                        
                                                
        
