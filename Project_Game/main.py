from LOGIC.logic import play_rps

def print_header():
    print("\n" + "*"*35)
    print(" STONE - PAPER - SCISSORS ")
    print("*"*35)

def main():
    while True:
        print_header()
        print("1. Play Game")
        print("2. Exit")
        
        menu_choice = input("\nEnter choice (1-2): ")
        
        if menu_choice == '1':
            user_move = input("Enter Stone, Paper, or Scissors: ").strip()
            result, comp_move, status = play_rps(user_move)
            
            if status == "Success":
                print("\n--- ROUND RESULTS ---")
                print(f"Your Move     : {user_move.capitalize()}")
                print(f"Computer Move : {comp_move.capitalize()}")
                print(f"Result        : >>> {result} <<<")
                print("---------------------")
            else:
                print(f"\n[ERROR] {status} Please try again.")
                
        elif menu_choice == '2':
            print("\nThanks for playing! Exiting...")
            break
        else:
            print("\n[ERROR] Invalid input.")

if __name__ == "__main__":
    main()