# def isPalindrome(s):
#     # print(s)
#     i = 0
#     j = len(s) - 1

#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1

#     return True


# def getPalindromesCount(s):
# Write your code here
# n = len(s)
# answer = 0
# dp = {}

# def f(index, string, dp):

#     print(index)
#     if index >= n:
#         if len(string) == 5:
#             if isPalindrome(string):
#                 return 1
#             # return 0
#         return 0

#     if len(string) > 5:
#         return 0

#     if (index, string) in dp:
#         print(dp)
#         return dp[(index, string)]

#     pick = f(index + 1, string + s[index], dp)
#     nopick = f(index + 1, string, dp)

#     dp[(index, string)] = (pick + nopick) % ((10**9) + 7)
#     return (pick + nopick) % ((10**9) + 7)

# return f(0, "", dp)
from itertools import combinations

# from math import comb
from collections import Counter


def getPalindromesCount(s):
    # Write your code here
    ctr = Counter([""])
    fives = 0
    for c in s:
        for ss, cnt in list(ctr.items()):
            ss += c
            if len(ss) < 5:
                ctr[ss] += cnt
            elif ss == ss[::-1]:
                fives += cnt

    return fives % ((10**9) + 7)


# s = "0000000100000010000000000000000000010000000001000010010000000000000000010000000001000000000001000000000000000000000000000000000001000000010000000000010000000000000000000000000100010000000000000000000000000000101000000100000000000000000100001000000000010000000000000000000000000001000000000000000010100100000000000000001000001000010000000000000000001000100101000000000010000000100001000000000011000100000000000000000000100001000000010000000010100010001000010000000000001000101000010000100000000001001000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000100000000000001000001000000000000000011010000000000000000001000000000000000000001100010000000000100000000000000000100000000000010000001000010000000001010001100000100000010000000001000000000000000000000001100000010001000000000100000100000010000000000000000000000000001000000000000001000000010000000000000000001100001010000101000000000001000000000000100000000110000000000000100000000"
s = "010110"
print(getPalindromesCount(s))
