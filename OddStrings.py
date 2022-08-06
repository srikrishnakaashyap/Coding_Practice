class OddStrings:

    def oddStrings(self, m, s):
        isEven = [False for i in range(len(s))]

        for i in range(len(s)):

            for j in s[i]:

                if ord(j) % 2 == 0:
                    isEven[i] = True
                    break

        odd = 0
        for i in range(len(s)):
            if isEven[i] == False:
                odd += 1

        if odd % 2 == 0:
            return "EVEN"
        return "ODD"


if __name__ == "__main__":

    os = OddStrings()

    s = ["abc", "abcd"]

    m = 2

    print(os.oddStrings(m, s))
