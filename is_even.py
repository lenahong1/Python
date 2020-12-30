number = input("Input your number: ")

try:
    number = int(number)
except ValueError:
    print("This is not a number, exiting...")
    exit()
