import random
import math

def lucky_number(n1, n2):
    random.seed()
    return random.randrange(n1, n2)


def check_integer(num):
    if not num.isdigit():
        raise Exception('Try again please, You entered a non-number!!')
    elif not isinstance(int(num), int):
        raise Exception('Try again!! Your number has either fractions or is negative!')
    return int(num)


def sort_numbers(my_list):
    my_list.sort()
    return my_list


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
    if the_list[1] - the_list[0] > 100:
        bonus_list.append(100)
    if the_list[1] - the_list[0] > 10:
        bonus_list.append(1)
    return sum(bonus_list)

def final_massages(num):
    if num < 200000:
        message = 'The jackpot score is 1000.000, you scored only {result}, better luck next time!!'
    elif num < 500000:
        message = 'The jackpot score is 1000.000, you scored {result}.Not bad! maybe you get even luckier next time!!'
    elif num < 1000000:
        message = 'The jackpot score is 1000.000, you scored {result}.Pretty cool!! Trust your luck!'
    else:
        message = '!!! CONGRATS!!! You got the jackpot of 1000.000, you lucky one!!!'
    return message


def get_inputs():
    n1 = input('Please choose any positive number: ')
    n2 = input('Please choose another positive number: ')
    n3 = input('Please choose another positive number: ')
    n1 = check_integer(n1)
    n2 = check_integer(n2)
    n3 = check_integer(n3)
    return n1, n2, n3


if __name__ == '__main__':
    while True:
        try:
            n1, n2, n3 = get_inputs()
            lucky_list = [n1, n2, n3]
            lucky_list.sort()
            lucky_num = lucky_number(lucky_list[0], lucky_list[2])
            score = lucky_game([lucky_num, lucky_list[1]])
            message = final_massages(score)
            message = message.format(result=score)
            print(message)
        except Exception as err:
            print(err)

