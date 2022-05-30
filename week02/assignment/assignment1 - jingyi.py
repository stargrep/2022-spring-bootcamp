# Assignment 1
# This assignment is for exercising Python fundamental I and getting familiar with Python syntax.

# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.

# Q1. Write a program which can compute the factorial of a given numbers.


def factorial(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(9) == 362880


# Q2. Write a program which take a num and print a str as the sum of all numbers from 1 to this number
# [1 + 2 + ... + x] and x is always >= 1.

def print_sum(x: int) -> str:
    li = [i for i in range(x+1)]
    return str(sum(li))


assert print_sum(1) == "1"
assert print_sum(3) == "6"
assert print_sum(5) == "15"


# Q3. Write a program to check is a year is leap year (x is always > 0)

def is_leap_year(year: int) -> bool:
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    return False


assert is_leap_year(2000)
assert is_leap_year(1996)
assert not is_leap_year(1900)
assert not is_leap_year(2001)


# Q4. Write a program to convert a list of lowercase words to uppercase words.

def to_upper_case(words: [str]) -> [str]:
    words = [word.upper() for word in words]
    return words


assert to_upper_case(["abc", "de"]) == ["ABC", "DE"]
assert to_upper_case(["Amazon", "Apple"]) == ["AMAZON", "APPLE"]


# Q5. Write a program to use only 'and' and 'or' to implement 'xor'
# https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fromtitle=xor&fromid=64178

def xor(a: bool, b: bool) -> bool:
    if (a and b) or (not a and not b):
        return False
    return True


assert not xor(True, True)
assert xor(True, False)
assert xor(False, True)
assert not xor(False, False)


# Q6. Write a Python program to display the current date and time under standard ISO 8601. e.g. 2021-12-03T10:15:30Z

import datetime
def get_current_time() -> str:
    res = datetime.datetime.now().replace(microsecond=0).isoformat()
    res = str(res)
    res += 'Z'
    return res


assert "T" in get_current_time()
assert "Z" in get_current_time()
assert 20 == len(get_current_time())

# Q7. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# please define function and test yourself.

def mySum(a:int, b:int) -> int:
    c = a + b
    if 15 <= c <= 20:
        return 20
    return c

assert mySum(10, 5) == 20
assert mySum(10, 9) == 20
assert mySum(3, 4) == 7
assert mySum(20, 30) == 50