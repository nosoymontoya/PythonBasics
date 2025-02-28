import random

number = random.randint(1,101)
success = False
tries = 0
remainingTries = 10
msg1 = '---\nCongratulations, you have won!\n'
msg2 = '---\nYou are really close, keep trying'
msg3 = '---\nYou are close, keep trying'
msg4 = '---\nYou are not close, keep trying'
msg5 = 'You have {} tries remaining\n---'
msg6 = '---\nSorry, you are out of tries\n'

print('Welcome\n')
while success is False and remainingTries > 0:
    print(msg5.format(remainingTries))
    guess = int(input('Please enter a number between 1 and 100: '))

    if guess == number:
        print(msg1)
        success = True
    elif abs(guess-number) <= 5:
        print(msg2)
    elif 5 < abs(guess-number) <15:
        print(msg3)
    else:
        print(msg4)
    tries += 1
    remainingTries -=1

if remainingTries == 0:
    print(msg6)