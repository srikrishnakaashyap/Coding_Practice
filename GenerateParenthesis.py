class GenerateParenthesis:

    def generateParenthesis(self, n):

        answer = []

        def f(string, op, cl):

            if op == n and cl == n:
                nonlocal answer
                answer.append(string)
                return

            if op > n or cl > n:
                return
            if op == 0:
                f(string + "(", op + 1, 0)
            if op == n:
                f(string + ")", op, cl + 1)

            if op > 0 and op < n:
                f(string + "(", op + 1, cl)

            if op > cl:
                f(string + ")", op, cl + 1)

        f("", 0, 0)
        return list(set(answer))


if __name__ == "__main__":

    gp = GenerateParenthesis()

    n = 3
    print(gp.generateParenthesis(n))
