number = 3
while True:
    guess = int(input("please enter 1-100: "))
    if number == guess:
        print("it's correct")
        break
    elif guess > 100 or guess < 0:
        print("guess out of range")
    else:
        print("it's incorrect")