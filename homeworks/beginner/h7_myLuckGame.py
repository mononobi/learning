import random
import math


def random_number(n1,n2):
    random.seed()
    output = [n1, n2]
    output.sort()
    return random.randrange(output[0], output[1])


def check_integer(num):
    if not num.isdigit():
        raise Exception('Error! You entered a non-number!!')
    # TODO: wrong assertion. catch ValueError instead.
    elif not isinstance(int(num), int):
        raise Exception('Error! Your number has either fractions or is negative!')
    return int(num)


def my_list(num1, num2, num3):
    random.seed()
    num1 = num1 + random.randrange(1, 100)
    num2 = num2 + random.randrange(1, 100)
    num3 = num3 + random.randrange(1, 100)
    l_list = [num1, num2, num3]
    l_list.sort()
    rand_number = random_number(l_list[0], l_list[2])
    compare_number = l_list[1]
    return [rand_number, compare_number]


def lucky_game(the_list):
    the_list.sort()
    bonus_list = []
    if the_list[0] == the_list[1]:
        bonus_list.append(800000)
    if math.isqrt(the_list[1]) == the_list[0]:
        bonus_list.append(500000)
    if the_list[1] % the_list[0] == 0:
        bonus_list.append(200000)
    if the_list[1] - the_list[0] > 1000:
        bonus_list.append(1000)
    elif the_list[1] - the_list[0] > 100:
        bonus_list.append(100)
    elif the_list[1] - the_list[0] > 10:
        bonus_list.append(the_list[1] - the_list[0])
    return sum(bonus_list)


def final_massages(num):
    if num < 1000:
        message1 = '\nThe jackpot score is 1000.000, you scored only {result}, better luck next time!\n'
    elif num < 200000:
        message1 = '\nThe jackpot score is 1000.000, you scored only {result}, I bet you could do better next time!\n'
    elif num < 500000:
        message1 = '\nThe jackpot score is 1000.000, you scored {result}.Not bad! ' \
                  '\nmaybe you d be even luckier next time!\n'
    elif num < 1000000:
        message1 = '\nThe jackpot score is 1000.000, you scored {result}.Pretty cool!! In your luck you may trust!\n'
    else:
        message1 = '\n!!! CONGRATS!!! You got the jackpot of 1000.000 scores, you lucky one!!!!!!!!!\n'
    return message1


def get_inputs():
    n1 = input('Please choose any desired positive number: ')
    n1 = check_integer(n1)
    n2 = input('Please choose another one: ')
    n2 = check_integer(n2)
    n3 = input('...and another one: ')
    n3 = check_integer(n3)
    return n1, n2, n3


def get_ok():
    q = input('Press "Enter" to start a new round of the game: \n\n')


def continue_ok(i):
    return True

#print(continue_ok('OK'))


if __name__ == '__main__':
    #while True:  ## how to waite for an Enter and then start over again??
    while continue_ok(get_ok()):
        try:
            print('Here is the our little lottery game:\nYou choose any 3 positive numbers, we calculate your score.'
                  ' Only your luck decides on what you get!\nHere you go, good luck!! \n')
            n1, n2, n3 = get_inputs()
            luck_list = my_list(n1, n2, n3)
            score = lucky_game(luck_list)
            message = final_massages(score)
            message = message.format(result=score)
            print(message)
        except Exception as err:
            print(err)

