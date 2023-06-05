# Advanced python concepts
'''Write a Python class called BankAccount with methods for depositing, 
withdrawing, and checking the account balance. '''

class BankAccount:
    def __init__(self, account_owner, account_type, current_amount):
        self.account_owner = account_owner 
        self.account_type = account_type 
        self.current_amount = current_amount  
    
    def deposit(self): 
        #This method ask for the amount of money the user wants to deposit
        # Also checks if user made a mistake with the amount or if user does not want to do the transaction anymore  
        
        while True:
            amount = float(input('Insert the amount to deposit: '))
            confirmation = input(f'Do you confirm you want to deposit {amount} to your account?: ').lower()
            
            if confirmation == 'yes':
                self.current_amount += amount
                print(f"{amount} has been succesfully deposited to your account")
                break

            elif confirmation == 'no':
                print(f'Transaction stopped')
                continue_t = input('Do you want to enter another amount?: ').lower()
                if continue_t == 'yes' :
                    continue
                elif continue_t == 'no' :
                    print('Transaction canceled')
                    break   
            else: 
                print('invalid, please type "yes" or "no" ')
               
    def withdrawing(self):
        #This method ask for the amount of money the user wants to deposit
        # Also checks if user made a mistake with the amount or if user does not want to do the transaction anymore  
        while True:
            amount = float(input('Insert the amount to withdraw: '))
            confirmation = input(f'Do you confirm you want to withdraw {amount} from your account?: ').lower()
            
            if confirmation == 'yes':
                self.current_amount -= amount
                print(f'{amount} has been succesfully withdrawed from your account')
                break

            elif confirmation == 'no':
                print('Transaction stopped')
                continue_t = input('Do you want withdraw another amount?: ').lower()
                
                if continue_t == 'yes' :
                    continue
                elif continue_t == 'no' :
                    print('Transaction canceled')
                    break
            else: 
                print('invalid, please type "yes" or "no"')

    def balance(self):
        print(f'account owner: {self.account_owner}, account type: {self.account_type}, current balance:{self.current_amount}')



usuario_1 = BankAccount("Pedro", "saving account", 100.00)
usuario_1.deposit()
usuario_1.withdrawing()
usuario_1.balance()


