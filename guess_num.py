import random
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue
num = random.randint(1,n)
while True:
    try:
        guess = int(input("guess: "))
        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
