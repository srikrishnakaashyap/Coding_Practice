class Sieve:

    ma = 10000000
    array = [1 for i in range(ma)]
    # print(array)
    compute = False

    def sieve(self):
        self.compute = True

        p = 2
        while(p*p <= self.ma):
            if self.array[p] == 1:
                k = p * p  # 6
                while(k < self.ma):
                    self.array[k] = 0
                    k += p  # 9, 12, 15, 18, 21, 24
            p += 1

    def isPrime(self, num):
        if not self.compute:
            self.sieve()

        print(self.array)

        return True if self.array[num] == 1 else False


if __name__ == "__main__":
    s = Sieve()

    print(s.isPrime(7))
