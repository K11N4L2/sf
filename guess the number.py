import random

print("Hi, please enter your name")
name = input()                       #input 1
secretNumber = random.randint(1, 50)
print(name + ' Guess the number between 1 & 50', '\nYou have 4 tries')
attempts = 0

for attempts in range(1, 5):
    print('Take a guess')
    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            print('Please Enter a Number')
            continue
    if guess < secretNumber:
        print('Too Low, you have ' + str(4 - attempts) + ' attempts remaining')
    elif guess > secretNumber:
        print('Too High, you have ' + str(4 - attempts) + ' attempts remaining')
    else:
        break

if guess == secretNumber:
    print('Well Done ' + name)
else:
    print('Too Many Attempts ' + str(attempts) + ', It was ' + str(secretNumber))
    play = False

# add something extra