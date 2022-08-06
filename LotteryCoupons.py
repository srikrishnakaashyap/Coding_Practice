class LotteryCoupons:

    def sumOfNumber(self, n):

        s = 0

        while(n > 0):
            i = n % 10
            n = n//10
            s += i
        return s

    def lotteryCoupons(self, n):

        hm = {}

        maxi = 0
        for i in range(1, n+1):
            s = self.sumOfNumber(i)
            if s in hm:
                hm[s] += 1

            else:
                hm[s] = 1

            maxi = max(maxi, hm[s])
        ans = 0
        for key, value in hm.items():
            if value == maxi:
                ans += 1

        return ans


if __name__ == "__main__":

    lc = LotteryCoupons()

    n = 11

    print(lc.lotteryCoupons(n))

    # print(lc.sumOfNumber(12))
