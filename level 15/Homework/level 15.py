number = 67
guess = input("guess number 1-100: ")

if guess == 67:
    print("correct!")
elif guess > 100:
    print("its out of range")
else:
   print("incorrect!")
   
kg = int(input("enter your weight: "))
meter = int(input("enter your height: "))
print(kg / (meter * meter))