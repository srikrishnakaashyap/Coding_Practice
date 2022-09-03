class RegularExpressionMatching:
    def isMatch(self, s, p):
        def f(i, j):

            if i == 0 and j == 0:
                if s[i] == p[j] or p[j] == "." or p[j] == "*":
                    return True
                return False

            if i == 0:
                if p[: j + 1] == "*" * (j + 1):
                    return True
                return False

            if j == 0:
                if p[j] == "*":
                    return True
                return False

            if p[j] == "." or s[i] == p[j]:
                return f(i - 1, j - 1)

            if p[j] == "*":
                return f(i - 1, j) or f(i - 1, j - 1)

            return False

        m = len(s)
        n = len(p)

        return f(m - 1, n - 1)


if __name__ == "__main__":

    re = RegularExpressionMatching()

    s = "aa"
    p = "a*"

    print(re.isMatch(s, p))
