"""
Pseudocode
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Please enter your name: ")
menu = """(H)ello - says hello
(G)oodbye - says goodbye
(Q)uit - exits the program"""
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid option")
    print(menu)
    choice = input(">>>").upper()
print(f"Thank you {name} for using the program")

