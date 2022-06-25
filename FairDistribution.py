import math


class FairDistribution:

    def distributeCookies(self, cookies, k):
        n = len(cookies)
        karr = [0 for i in range(k)]
        dp = dict()

        def f(index):
            t = tuple(sorted(karr))
            if t in dp:
                return dp[t]

            if index == n:
                return max(karr)

            answer = math.inf

            for ind in range(k):
                karr[ind] += cookies[index]
                answer = min(answer, f(index + 1))
                karr[ind] -= cookies[index]

            dp[t] = answer
            return answer

        return f(0)


if __name__ == "__main__":

    fd = FairDistribution()

    cookies = [20, 9, 4, 20, 16, 20, 18]
    k = 3

    print(fd.distributeCookies(cookies, k))
