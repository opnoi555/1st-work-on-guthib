import random

HEADS = 1
TAILS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEADS,TAILS) == HEADS:
            print('HEADS')
        else:
            print('TAILS')

tosses_coin()