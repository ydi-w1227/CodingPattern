# Any number will be called a happy number if, after repeatedly replacing it with a number
# equal to the sum of the square of all of its digits, leads us to number ‘1’.
# All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
#
# Example 1:
#
# Input: 23
# Output: true (23 is a happy number)
# Explanations: Here are the steps to find out that 23 is a happy number:

# 2^​2​​ +3^​2 = 4 + 9 = 13
# 1^2 + 3^2 = 1 + 9 = 10
# 1^2 + 0^2​​ = 1 + 0 = 1

# Example 2:
#
# Input: 12
# Output: false (12 is not a happy number)
# Explanations: Here are the steps to find out that 12 is not a happy number:
# 1^2 + 2 ^2 = 1 + 4 = 5
# 5^2 = 25
# 2^2 + 5^2 = 4 + 25 = 29
# 2^2 + 9^2 = 4 + 81 = 85
# 8^2 + 5^2 = 64 + 25 = 89 --- duplicate
# 8^2 + 9^2 = 64 + 81 = 145
# 1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
# 4^2 + 2^2 = 16 + 4 = 20
# 2^2 + 0^2 = 4 + 0 = 4
# 4^2 = 16
# 1^2 + 6^2 = 1 + 36 = 37
# 3^2 + 7^2 = 9 + 49 = 58
# 5^2 + 8^2 = 25 + 64 = 89 --- duplicate
# last step, Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’,
# this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.

import math

def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = count_sqrt_1(slow)
        fast = count_sqrt_1(count_sqrt_1(fast))
        print('slow is: ', slow)
        print('fast is: ', fast)
        if slow == 1 or fast == 1:
            return True
        if slow == fast:
            break
    return False

def count_sqrt_1(num):
    # O(logN)
    # -> https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn
    # -> https://stackoverflow.com/questions/58977656/how-to-understand-time-complexity-of-happy-number-problem-solution-from-leetcode
    current_sum = 0
    while num > 0:
        digit = num % 10
        current_sum += digit * digit
        num = num // 10
    return current_sum

def count_sqrt_2(num):
    digits = [int(d) for d in str(num)]
    current_sum = 0
    for digit in digits:
        current_sum += math.sqrt(digit)
    return current_sum

# from wiki
def ishappy(n):
    a = []
    while n not in a:
        a.append(n)
        n = sum([int(x) ** 2 for x in str(n)])

    return 'happy' if n == 1 else 'unhappy'

def find_happy_number_2(num):
    check = set()
    while num not in check:
        check.add(num)
        num = count_sqrt_1(num)
        if num == 1:
            return True
    return False

def main():
    print(find_happy_number(23))
    print(find_happy_number_2(23))
    print(find_happy_number(12))
    print(find_happy_number_2(12))



main()