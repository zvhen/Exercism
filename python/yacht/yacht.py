# Score categories.
# Change the values as you see fit.

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def handle_YACHT(dice):
    dice.sort()
    if unique(dice) == 1:
        return 50
    else:
        return 0

def handle_ONES(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 1:
            count += 1
    if count > 0:
        return count*1
    else:
        return 0

def handle_TWOS(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 2:
            count += 1
    if count > 0:
        return count*2
    else:
        return 0    

def handle_THREES(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 3:
            count += 1
    if count > 0:
        return count*3
    else:
        return 0

def handle_FOURS(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 4:
            count += 1
    if count > 0:
        return count*4
    else:
        return 0

def handle_FIVES(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 5:
            count += 1
    if count > 0:
        return count*5
    else:
        return 0

def handle_SIXES(dice):
    count = 0
    dice.sort()
    for numbers in dice:
        if numbers == 6:
            count += 1
    if count > 0:
        return count*6
    else:
        return 0

def handle_FULL_HOUSE(dice):
    if unique(dice) == 2 and (count_same_dice(dice) == 3 or count_same_dice(dice) == 2):
        return sum(dice)
    else:
        return 0

def handle_FOUR_OF_A_KIND(dice):
    if (unique(dice) == 2 or unique(dice) == 1) and (count_same_dice(dice) == 4 or count_same_dice(dice) == 5):
        return sum(dice[:4])
    elif (unique(dice) == 2 or unique(dice) == 1) and (count_same_dice(dice) == 1):
        return sum(dice[1:])
    else:
        return 0

def handle_LITTLE_STRAIGHT(dice):
    dice.sort()
    if unique(dice) == 5 and dice[0] == 1 and dice[4] == 5:
        return 30
    else:
        return 0

def handle_BIG_STRAIGHT(dice):
    dice.sort()
    if unique(dice) == 5 and dice[0] == 2 and dice[4] == 6:
        return 30
    else:
        return 0

def handle_CHOICE(dice):
    return sum(dice)

def unique(dice):
    unique = 1
    dice.sort()
    for index in range(1,len(dice)):
        if dice[index] != dice[index-1]:
            unique += 1
    return unique

def count_same_dice(dice):
    count = 1
    dice.sort()
    for index in range(1,len(dice)):
        if dice[index] == dice[index-1]:
            count += 1
        else:
            return count
    return count



def score(dice, category):
    myDict = {
    0 : handle_YACHT,
    1 : handle_ONES,
    2 : handle_TWOS,
    3 : handle_THREES,
    4 : handle_FOURS,
    5 : handle_FIVES,
    6 : handle_SIXES,
    7 : handle_FULL_HOUSE,
    8 : handle_FOUR_OF_A_KIND,
    9 : handle_LITTLE_STRAIGHT,
    10 : handle_BIG_STRAIGHT,
    11 : handle_CHOICE
    }

    chosen_score = myDict.get(category,None)
    return chosen_score(dice)

print(count_same_dice([1, 4, 4, 4, 4]))
print(score([1, 4, 4, 4, 4], FULL_HOUSE))

