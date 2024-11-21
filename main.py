from colorama import Fore, Back, Style, init

init(autoreset=True)

def main():
    gusts = ["Shoaib", "Fateh", "Omid", "Osman"]

    while True:
        # options
        print(Back.CYAN + Fore.BLACK + "[1] Add guest.")
        print(Back.YELLOW + Fore.BLACK + "[2] Remove guest.")
        print(Back.GREEN + Fore.BLACK + "[3] Show guest list.")
        print(Back.MAGENTA + Fore.BLACK + "[4] Check if someone is on the list.")
        print(Back.RED + Fore.BLACK + "[5] Exit.")




        option = input(Fore.BLUE + "Choose an option [1-5]: ")

        # addi gusts
        if option == "1":
            new_gust = input(Fore.YELLOW + "Enter Gust Full Name to add: ")
            gusts.append(new_gust)

            print(Fore.GREEN + f"{new_gust} added.")

        # removing gusts
        elif option == "2":
            remove_gust = input(Fore.YELLOW + "Enter Gust Full Name to remove: ")

            if remove_gust in gusts:
                gusts.remove(remove_gust)
                print(Fore.RED + f"{remove_gust} removed!")
            else:
                print(Fore.RED + f"{remove_gust} not found.")

        # showing gusts list
        elif option == "3":    
            if gusts:
                print(Fore.CYAN + "Guest list:")

                for gust in gusts:
                    print(Fore.GREEN + gust)

            else:
                print(Fore.RED + "No guests yet.")

        # searching gust's list
        elif option == "4": 
            find_gust = input(Fore.YELLOW + "Enter Gust Full Name to find: ")
            if find_gust in gusts:
                print(Fore.GREEN + f"{find_gust} is on the list.")
            else:
                print(Fore.RED + f"{find_gust} not registered.")

        # exit
        elif option == "5":
            print(Fore.CYAN + "Goooood bye!")
            break

        else:
            print(Fore.RED + "Invalid option, try again.")





main()
