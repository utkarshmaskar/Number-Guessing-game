import random

number = int(input("Enter a number: "))
secret = random.randint(0, number)

for attempt in range(3):
    guess = int(input(f"Attempt {attempt + 1}: Take a guess: "))
    
    if guess == secret:
        print("Oouuuu, you got it right!")
        break
    elif guess > secret:
        print("Oh no, you are above the number.")
    else:
        print("Oh boy, you are below the number.")

else:
    print(f"Sorry! You've used all 3 chances. The number was {secret}.")

             
