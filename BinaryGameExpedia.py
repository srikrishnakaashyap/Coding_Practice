def f(currString, size, one_group, zero_group, dp):
    if len(currString) == size:
        return 1

    if (currString, size) in dp:
        return dp[(currString, size)]

    if len(currString) > size:
        return 0

    zeroGroup = f(currString + "0" * zero_group, size, one_group, zero_group, dp)
    oneGroup = f(currString + "1" * one_group, size, one_group, zero_group, dp)

    dp[(currString, size)] = zeroGroup + oneGroup

    return zeroGroup + oneGroup


def countGoodStrings(min_length, max_length, one_group, zero_group):
    # Write your code here

    answer = 0
    dp = {}

    for i in range(min_length, max_length + 1):
        answer += f("", i, one_group, zero_group, dp)

    return answer % 1000000007
