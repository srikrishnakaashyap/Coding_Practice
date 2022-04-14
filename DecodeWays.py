from pyparsing import opAssoc


class DecodeWays:

    # def decodeWays2(self, s):

    #     def dp(i):
    #         if i == len(s):
    #             return 1
    #         ans = 0
    #         if s[i] != '0':  # Single digit
    #             ans += dp(i + 1)
    #         # Two digits
    #         if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):
    #             ans += dp(i + 2)
    #         return ans

    #     return dp(0)

    def decodeWays(self, s):

        def f(index):
            if index < 0:
                return 1

            if dp[index] != -1:
                return dp[index]

            oneIndex = 0
            if int(s[index]) != 0:
                oneIndex = f(index - 1)

            twoIndex = 0
            if index > 0 and (int(s[index - 1]) == 1 or int(s[index - 1]) == 2 and int(s[index]) <= 6):
                twoIndex = f(index - 2)

            dp[index] = oneIndex + twoIndex
            return oneIndex + twoIndex

        n = len(s)
        dp = [-1 for i in range(n)]
        answer = f(n - 1)
        return answer


if __name__ == "__main__":

    dw = DecodeWays()
    s = "2611055971756562"

    print(dw.decodeWays(s))
