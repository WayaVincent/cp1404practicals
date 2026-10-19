for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("a)")
for i in range (0,101, 10):
    print(i, end=' ')
print()

print("b)")
for i in range (20, 0, -1):
    print(i, end=' ')
print()

print("c)")
stars = int(input("Please enter a number: "))
for i in range (0, stars, 1):
    print("*", end = " ")
print()

print("d)")
lines = int(input("Please enter a number: "))
for i in range (1, lines+1, 1):
    for j in range (0, i, 1):
        print ("*", end = " ")
    print()
print()
