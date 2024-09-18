import time

def task_1():
    password = "Password123"

    # Enter your code here
    guess = input("Guess the password: ")
    while not guess == password:
        print("Password incorrect, try again!")
        guess = input("Guess the password: ")
    else:
        print("Password cracked!")


def task_2(): # Times table

    # Enter your code here
    number = int(input("What number to you want multiply?: "))
    times = int(input("How many times do you want to multiply it?: "))
    count = 0
    while count < times:
        count += 1
        print(number * count)
        

def task_3(): # Count mississippis
    count = 0
    while count < 5:
        count += 1
        print(f"{count} mississippi")
        time.sleep(1)

task_1()