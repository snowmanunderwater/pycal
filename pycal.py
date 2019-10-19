#!/usr/bin/env python3

from datetime import datetime
from operator import add, mul, sub, truediv
from random import choice, randint
from time import time as timecounter
import argparse

operations = ((add, '+'), (sub, '-'), (mul, '*'), (truediv, '/'))
today = datetime.today()

HISTORY_FILE = 'data'


# table headers
# operation, a, b, user_answer, correct_answer, difference, cur_date, cur_time, time_for_complite
def write_to_history(data):
    with open(HISTORY_FILE, 'a') as f:
        f.write(','.join(map(str, data)) + '\n')


# !FIXME
# протестировать при всех случаях
#  a, b
# -a, b
#  a, -b
# -a, -b
def calc_difference(a, b):
    return round((a - b) / a * 100, 2)


def main():
    while True:
        try:
            operation = choice(operations)
            a = randint(2, 100)
            b = randint(2, 100)

            correct_answer = round(operation[0](a, b), 2)

            print(f"{a} {operation[1]} {b} = ", end='')

            time_start = timecounter()

            user_answer = input()

            if user_answer.isidentifier():
                print('Bye')
                exit()

            # user input
            try:
                user_answer = float(user_answer)
            except ValueError:
                print('Only numbers awailable.')
                continue

            time_end = timecounter()

            time_for_complite = round(time_start - time_end, 2)
            cur_date = today.date().isoformat()
            cur_time = today.time().isoformat('seconds')
            difference = calc_difference(user_answer, correct_answer)

            write_to_history(
                (operation[1], a, b, user_answer, correct_answer, difference,
                 cur_date, cur_time, time_for_complite))

        except (KeyboardInterrupt, EOFError):
            print('\nBye')
            exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--clear",
                        help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    main()
