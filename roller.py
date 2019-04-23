import random

question = input('Would you like to roll the dice? [y/n]\n')

while question != 'n':
    if question == 'y':
        print('\nBegin rolling......\n')
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 20)
        die3 = random.randint(1, 10)
        die4 = random.randint(1, 12)
        die5 = random.randint(1, 8)
        die6 = random.randint(1, 4)
        print('Here are your results:\n')
        print(die1)
        print(die2)
        print(die3)
        print(die4)
        print(die5)
        print(die6)
        print('\n')
        question = input('Would you like to roll the dice? [Y/N]\n')
    else:
        print('Invalid response! Please type "Y" for YES or "N" for NO.')
        question = input('Would you like to roll the dice? [Y/N]\n')

print('Good-bye!')
