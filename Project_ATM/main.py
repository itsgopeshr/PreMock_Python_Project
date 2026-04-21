from LOGIC.logic import ATM

def print_header(title):
    print("\n" + "="*30)
    print(f"{title:^30}")
    print("="*30)

def main():
    my_atm = ATM()
    
    while True:
        print_header("ATM MAIN MENU")
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Mini Statement")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            print(f"\n[INFO] Current Balance: ₹{my_atm.display_balance():.2f}")
            
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if my_atm.withdraw(amount):
                    print(f"\n[SUCCESS] ₹{amount:.2f} withdrawn successfully.")
                else:
                    print("\n[ERROR] Invalid amount or insufficient balance.")
            except ValueError:
                print("\n[ERROR] Please enter a valid number.")
                
        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if my_atm.deposit(amount):
                    print(f"\n[SUCCESS] ₹{amount:.2f} deposited successfully.")
                else:
                    print("\n[ERROR] Invalid amount.")
            except ValueError:
                print("\n[ERROR] Please enter a valid number.")
                
        elif choice == '4':
            print_header("MINI STATEMENT")
            transactions = my_atm.get_statement()
            if not transactions:
                print("No transactions yet.")
            else:
                for t in transactions:
                    print(t)
            print(f"Closing Balance: ₹{my_atm.display_balance():.2f}")
            
        elif choice == '5':
            print("\nThank you for using the ATM. Goodbye!")
            break
            
        else:
            print("\n[ERROR] Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()