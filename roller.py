import random

#question = input('Would you like to roll the dice? [y/n]\n')

#while question != 'n':
    #if question == 'y':
def dieRoller():
    stats = []
    print('\nBegin rolling......\n')
    # die1 = random.randint(1, 6)
    # die2 = random.randint(1, 20)
    # die3 = random.randint(1, 10)
    # die4 = random.randint(1, 12)
    # die5 = random.randint(1, 8)
    # die6 = random.randint(1, 4)
    count = 0
    while(count < 6):
        temp_dice = []
        temp_stats = 0
        diceCount = 0
        while(diceCount < 4):
            temp_dice.append(random.randint(1,6))
            diceCount += 1
        temp_dice.remove(min(temp_dice))
        for die in temp_dice:
            temp_stats += die
        stats.append(temp_stats)
        count += 1
    print('Here are your results:\n')
    for stat in stats:
        print(stat)
    # print(die1)
    # print(die2)
    # print(die3)
    # print(die4)
    # print(die5)
    # print(die6)
    print('\n')
    return stats
    #question = input('Would you like to roll the dice? [Y/N]\n')
# else:
    #print('Invalid response! Please type "Y" for YES or "N" for NO.')
    #question = input('Would you like to roll the dice? [Y/N]\n')

#print('Good-bye!')
