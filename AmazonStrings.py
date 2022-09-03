class AmazonStrings:
    def compareStrings(self, oldPassword, newPassword):

        m = len(oldPassword)
        n = len(newPassword)

        op = 0
        np = 0

        while op < m and np < n:

            if (
                oldPassword[op] == newPassword[np]
                or ord(oldPassword[op]) - ord(newPassword[np]) == 1
            ):
                op += 1
                np += 1
            elif newPassword[np] == "z" and oldPassword[op] == "a":
                op += 1
                np += 1
            else:
                np += 1

        if op == m:
            return "YES"

        return "NO"

    def compareStrings2(self, oldPassword, newPassword):

        m = len(oldPassword)
        n = len(newPassword)

        op = 0
        np = 0

        while op < m and np < n:

            if (
                oldPassword[op] == newPassword[np]
                or ord(oldPassword[op]) - ord(newPassword[np]) == 1
            ):
                op += 1
                np += 1
            elif newPassword[np] == "z" and oldPassword[op] == "a":
                op += 1
                np += 1
            else:
                np += 1

        if op == m:
            return "YES"

        return "NO"

    def amazonStrings(self, oldPasswords, newPasswords):

        n = len(oldPasswords)

        answer = [0 for i in range(n)]

        for i in range(n):
            answer[i] = self.compareStrings(oldPasswords[i], newPasswords[i])

        return answer


if __name__ == "__main__":

    obj = AmazonStrings()

    oldPasswords = ["abdbc", "ach", "abb"]

    newPasswords = ["baacbab", "accdb", "baacba"]

    print(obj.amazonStrings(oldPasswords, newPasswords))

    print(obj.compareStrings("a", "z"))
