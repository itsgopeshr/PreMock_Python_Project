from LOGIC.logic import Library

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def main():
    lib = Library()
    
    while True:
        print_header("LIBRARY MANAGEMENT SYSTEM")
        print("1. View Available Books")
        print("2. Issue a Book")
        print("3. Return a Book")
        print("4. Notice / Fine Policy")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            print_header("BOOK CATALOG")
            catalog = lib.display_books()
            print(f"{'ID':<10} | {'TITLE':<25} | {'STATUS'}")
            print("-" * 50)
            for b_id, details in catalog.items():
                status = "Available" if details["available"] else "Issued"
                print(f"{b_id:<10} | {details['title']:<25} | {status}")
                
        elif choice == '2':
            print_header("ISSUE BOOK")
            b_id = input("Enter Book ID: ").strip()
            s_name = input("Enter Student Name: ").strip()
            date_str = input("Enter Issue Date (YYYY-MM-DD): ").strip()
            
            try:
                days = int(input("Allotted Days for return: "))
                success, msg = lib.issue_book(b_id, s_name, date_str, days)
                if success:
                    print(f"\n[SUCCESS] {msg}")
                else:
                    print(f"\n[ERROR] {msg}")
            except ValueError:
                print("\n[ERROR] Allotted days must be an integer.")

        elif choice == '3':
            print_header("RETURN BOOK")
            b_id = input("Enter Book ID: ").strip()
            date_str = input("Enter Return Date (YYYY-MM-DD): ").strip()
            
            success, msg, fine = lib.return_book(b_id, date_str)
            
            if success:
                print(f"\n[INFO] {msg}")
                if fine > 0:
                    print(f"[ALERT] Late Fee Applied: ₹{fine}")
                else:
                    print("[SUCCESS] No fines applied.")
            else:
                print(f"\n[ERROR] {msg}")
                
        elif choice == '4':
            print_header("FINE POLICY")
            print("Return books within allotted days to avoid fines.")
            print("Fines are applied progressively per overdue day:")
            print("- Week 1 Late: ₹10 / day")
            print("- Week 2 Late: ₹20 / day")
            print("- Week 3 Late: ₹60 / day")
            
        elif choice == '5':
            print("\nClosing Library System. Goodbye!")
            break
            
        else:
            print("\n[ERROR] Invalid choice.")

if __name__ == "__main__":
    main()