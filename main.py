

def main():
    gusts = []

    while True:
        print("[1] Add guest.")
        print("[2] Remove guest.")
        print("[3] Show guest list.")
        print("[4] Check if someone is on the list.")

        option = input("Choose an option [1-4]: ")

        if option == "1":
            new_gust = input("Enter Gust Full Name: ")
            gusts.append(new_gust)

        
        for gust in gusts:
            print(gust)




main()


