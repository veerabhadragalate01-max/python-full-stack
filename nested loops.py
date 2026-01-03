# for i in range(5):
#     print(i)
#     for i in range(16,20):
#         print(i)
#         if i==17:
#             break

accounts = {
    '102012': {
        'name': 'mike',
        'balance': 10000
    },
    '102013': {
        'name': 'vamsi',
        'balance': 34.5
    },
    '102014': {
        'name': 'arun',
        'balance': 230500
    }
}



def show_menu():
        
    while True:
        print('''
            1. View Account Balance
            2. Transfer Amount
            3. Withdraw Amount
            4. Deposit Amount
            5. Exit
       ''')
        option = int(input('Choose an option:'))
        if option == 1:
            acc = input('Enter Acc number:')
            if acc in accounts:
                b = accounts[acc]['balance']
                print(f"Your balance is Rs.{b}/-")
            else:
                print('Account not found')
        elif option == 2:
            sa = input('Enter Source Account:')
            da = input('Enter Destination Account:')
            amount = int(input('Amount to Transfer'))
            accounts[sa]['balance'] -= amount
            accounts[da]['balance'] += amount
            print('Transfer successful.')
            pass
        elif option == 3:
            wd=input("plese enter your account number:")
            wd_amount=int(input("enter withdrwal amount:"))
            accounts[wd]['balance'] -= wd_amount
            remaing_balance = accounts[wd]['balance']
            print("Transaction completed")
            print(f'your available balance is Rs{remaing_balance}-/')
            pass
        elif option == 4:
            ATD=input("plese enter your account number:")
            ATD_AMOUNT=int(input("enter deposite amount"))
            print(f"your deposite amount RS {ATD_AMOUNT}-/-")
            accounts[ATD]['balance'] += ATD_AMOUNT
            available_balance = accounts[ATD]['balance']
            print("Trasnaction completed")
            print(f'your remaing balance Rs{available_balance}-/-')
            pass
        elif option == 5:
            print("EXIT")
            break
        else:
            print('Invalid option')




def main():
    show_menu()

#if "_name_"== "_main_":

main()
    