class CalculateAmount:

    def calculateAmount(self, brackets, income):
        answer = 0

        ctr = 0

        while(income > 0):

            if ctr == 0:
                m = min(income, brackets[0][0])
                answer += (brackets[0][1] * m) / 100
            else:
                m = min(income, brackets[ctr][0] - brackets[ctr - 1][0])
                answer += (brackets[ctr][1] * m) / 100
            income -= m
            ctr += 1

        return answer


if __name__ == "__main__":
    ca = CalculateAmount()

    brackets = [[2, 50]]
    income = 0

    print(ca.calculateAmount(brackets, income))
