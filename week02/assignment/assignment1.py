# Assignment 1
# This assignment is for exercising Python fundamental I and getting familiar with Python syntax.

# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.

# Q1. Write a program which can compute the factorial of a given numbers.


def factorial(x: int) -> int:
    if x<=1:
        return 1
    else:
        return x*factorial(x-1)


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(9) == 362880


# Q2. Write a program which take a num and print a str as the sum of all numbers from 1 to this number
# [1 + 2 + ... + x] and x is always >= 1.

def print_sum(x: int) -> str:
    return str(_sum(x))

def _sum(x):
    if x == 1:
        return 1
    return x + _sum(x - 1)


assert print_sum(1) == "1"
assert print_sum(3) == "6"
assert print_sum(5) == "15"


# Q3. Write a program to check is a year is leap year (x is always > 0)

def is_leap_year(year: int) -> bool:
    if not year%100:
        if year%400:
            return False
        else:
            return True
    else:
        if year%4:
            return False
        else:
            return True


assert is_leap_year(2000)
assert is_leap_year(1996)
assert not is_leap_year(1900)
assert not is_leap_year(2001)


# Q4. Write a program to convert a list of lowercase words to uppercase words.

def to_upper_case(words: [str]) -> [str]:
    uppp = []
    for i in words:
        uppp.append(i.upper())
    return uppp


assert to_upper_case(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]


# Q5. Write a program to use only 'and' and 'or' to implement 'xor'
# https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fromtitle=xor&fromid=64178

def xor(a: bool, b: bool) -> bool:
    return a != b

assert not xor(True, True)
assert xor(True, False)
assert xor(False, True)
assert not xor(False, False)


assert not xor(True, True)
assert xor(True, False)
assert xor(False, True)
assert not xor(False, False)


# Q6. Write a Python program to display the current date and time under standard ISO 8601. e.g. 2021-12-03T10:15:30Z

import re
import time

def get_current_time() -> str:
    time_tuple = time.localtime()
    year, mon, day, hour, minu, sec = time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4], \
                                      time_tuple[5]
    year = str(year).zfill(4)
    mon = str(mon).zfill(2)
    day = str(day).zfill(2)
    hour = str(hour).zfill(2)
    minu = str(minu).zfill(2)
    sec = str(sec).zfill(2)
    return year + "-" + mon + "-" + day + "T" + hour + ":" + minu + ":" + sec + "Z"


assert re.fullmatch(r'(\d){4}-(\d){2}-(\d){2}T(\d){2}:(\d){2}:(\d){2}Z', get_current_time())



assert "T" in get_current_time()
assert "Z" in get_current_time()
assert 20 == len(get_current_time())

# Q7. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# please define function and test yourself.
def two_num(a, b) -> str:
    c = a + b
    if 15 < c < 20:
        return 20
    else:
        return c
assert two_num(15, 4)==20
assert two_num(17, 1)==20
assert two_num(11, 4)==15