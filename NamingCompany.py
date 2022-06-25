class NamingCompany:

    def distinctNames(self, ideas):

        hm = {}

        for idea in ideas:
            hm[idea] = 1

        n = len(ideas)
        answer = 0
        for i in range(0, n):
            for j in range(0, n):

                if i != j:

                    word1 = ideas[i][0] + ideas[j][1:]
                    word2 = ideas[j][0] + ideas[i][1:]

                    if word1 not in hm and word2 not in hm:
                        answer += 1

        return answer


if __name__ == "__main__":
    nc = NamingCompany()

    ideas = ["coffee", "donuts", "time", "toffee"]

    print(nc.distinctNames(ideas))
