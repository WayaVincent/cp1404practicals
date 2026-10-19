
menu = """(E)ven - shows all even numbers between a start and end number
(O)dd - shows all odd numbers between a start and end number
(S)quare - shows the square of all the numbers between a start and end number
(Q)uit - Exits the program"""
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    x = int(input("Please input a number for the start of the sequence: "))
    y = int(input("Please input a number for the end of the sequence: "))
    if choice == "E":
        for i in range (x, y+1, 1):
            if i%2 == 0:
                print(i, end = " ")
        print()
    elif choice == "O":
        for i in range (x, y+1, 1):
            if i%2 == 1:
                print(i, end = " ")
        print()
    elif choice == "S":
        for i in range(x, y+1, 1):
            print(i**2, end=" ")
        print()
    else:
        print("Invalid option")
        print()
    print(menu)
    choice = input(">>>").upper()
print("Exiting sequencer")