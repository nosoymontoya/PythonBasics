#Rock Paper Scisors

import math
import random

r = 'Rock'
p = 'Paper'
s = 'Scisors'
scorePC = 0
scorePlayer = 0
scoreMsg = ('Player {} vs PC {}')

print('\nHello')

numberOfgames = int(input('Let\'s play the best out of '))
scoreLimit = math.ceil(numberOfgames/2)


print(scoreLimit)

while scorePlayer is not scoreLimit or scorePlayer is not scoreLimit:

    randompPick = random.choice([r,p,s])
    player = input('\nChoose between Rock, Paper, and Scisors:   ')
    print(randompPick)
    condition1 = player.lower() == r.lower() and randompPick.lower() == s.lower()
    condition2 = player.lower() == p.lower() and randompPick.lower() == r.lower()
    condition3 = player.lower() == s.lower() and randompPick.lower() == p.lower()
    condition4 = player.lower() == randompPick.lower()


    if condition4 is True:
        print('Seems lik a tie, lets keep playing\n---')
    elif condition1 is True or condition2 is True or condition3 is True:
        print('You win!\n---')
        scorePlayer += 1
        print(scoreMsg.format(scorePlayer,scorePC))
    else:
        print('You loose!\n---')
        scorePC += 1
        print(scoreMsg.format(scorePlayer,scorePC))
print('\nThe final tally is ', scoreMsg.format(scorePlayer,scorePC))