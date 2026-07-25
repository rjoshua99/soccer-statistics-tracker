from api import get_standings, get_scorers, get_matches
from display import show_standings, show_scorers, show_matches
from save import save_json, save_scorers_csv, save_matches_csv

def main():
    while True:
        print("\n--- Premier League Stats Tracker ---")
        print("1. View Standings")
        print("2. View Top Scorers")
        print("3. View Matches")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice =="1":
            data = get_standings()
            show_standings(data)

        elif choice == "2":
            data = get_scorers()
            show_scorers(data)

        elif choice == "3":
            matchday = input("Enter matchday number (or press Enter for all): ")
            data = get_matches()
            if matchday == "":
                show_matches(data)
            else:
                show_matches(data, int(matchday))

        elif choice == "4":
            print("Exit Successfuly")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
