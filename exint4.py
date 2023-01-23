# fourth commit
sum = 0
for i in range(5):
    while True:
        try:
            num = int(input("Enter  int # "))
            sum += num
            break
        except ValueError:
            print("Invalid input. Please enter an int.")
print("Your sum is:", sum)

#Sources https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://www.w3schools.com/python/python_try_except.asp