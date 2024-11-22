from colorama import Fore, Back, Style, init
import random

init(autoreset=True)

def main():
    guests = {}

    while True:
        print(Back.CYAN + Fore.BLACK + "[1] Add guest.")
        print(Back.YELLOW + Fore.BLACK + "[2] Remove guest.")
        print(Back.GREEN + Fore.BLACK + "[3] Show guest list.")
        print(Back.MAGENTA + Fore.BLACK + "[4] Check if someone is on the list.")
        print(Back.RED + Fore.BLACK + "[5] Exit.")

        option = input(Fore.BLUE + "Choose an option [1-5]: ")

        # Add guest
        if option == "1":
            new_guest = input(Fore.YELLOW + "Enter Guest Full Name to add: ")
            guests[f"person_{random.randint(100, 999)}"] = new_guest
            print(Fore.GREEN + f"{new_guest} added to the guest list.")

        # Remove guest
        elif option == "2":
            remove_guest = input(Fore.YELLOW + "Enter Guest Full Name to remove: ")
            # Find key corresponding to the guest
            for key, value in guests.items():
                if value == remove_guest:
                    del guests[key]
                    print(Fore.RED + f"{remove_guest} removed from the guest list!")
                    break
            else:
                print(Fore.RED + f"{remove_guest} not found in the guest list.")

        # Show guest list
        elif option == "3":
            if guests:
                print(Fore.CYAN + "Guest list:")
                for guest in guests.values():
                    print(Fore.GREEN + guest)
            else:
                print(Fore.RED + "No guests in the list yet.")

        # Search for a guest
        elif option == "4":
            find_guest = input(Fore.YELLOW + "Enter Guest Full Name to search: ")
            if find_guest in guests.values():
                print(Fore.GREEN + f"{find_guest} is on the guest list.")
            else:
                print(Fore.RED + f"{find_guest} not found in the guest list.")

        # exit
        elif option == "5":
            print(Fore.CYAN + "Goooood bye!")
            break

        else:
            print(Fore.RED + "Invalid option, try again.")





main()
