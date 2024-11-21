

def main():
    gusts = ["Shoaib", "Fateh", "Omid", "Osman"]

    while True:
        print("[1] Add guest.")
        print("[2] Remove guest.")
        print("[3] Show guest list.")
        print("[4] Check if someone is on the list.")
        print("[5] Exit.")

        option = input("Choose an option [1-4]: ")

        # adding gusts
        if option == "1":
            new_gust = input("Enter Gust Full Name to add: ")
            gusts.append(new_gust)

            print(f"{new_gust} added.")

        # removing gusts
        elif option == "2":
            remove_gust = input("Enter Gust Full Name to remove: ")

            if remove_gust in gusts:
                gusts.remove(remove_gust)
                print(f"{remove_gust} removed!")
            else:
                print(f"{remove_gust} not found.")

        # showing gusts list
        elif option == "3":    
            if gusts:
                print("Guest list:")

                for gust in gusts:
                    print(gust)

            else:
                print("No guests yet.")

        # searching gust's list
        elif option == "4": 
            find_gust = input("Enter Gust Full Name to find: ")
            if find_gust in gusts:
                print(f"{find_gust} is on the list.")



            else:
                print(f"{find_gust} not registered.")

        # exit
        elif option == "5":
            print("Goooood bye!")
            break


        else:
            print("Invalid option, try again.")

                


        





main()


