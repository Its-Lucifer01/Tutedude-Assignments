# Task 1: Checking Even/ odd

a = int(input("Enter a number here: "))

if a % 2 == 0:
    print(a, "is an Even Number.")
else:
    print(a, "is an odd number")


# Task 2: Sum of Integers from 1 to 50 Using a Loop
res = 0

for i in range(1, 51):
    res += i

print("The sum of integers from 1 to 50 is: ", res)