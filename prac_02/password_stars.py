"""Password program"""

#Constants
PASS_LENGTH_MIN = 8

password = input("Please enter your password: ")
if len(password) >= PASS_LENGTH_MIN:
    verify = input("Please re-enter your password: ")
    if password == verify:
        print("Success")
        for i in range(1, len(password)+1, 1):
            print("*", end = "")
    else:
        print ("Password does not match")
else:
    print("Password needs to have minimum 8 characters")

