class GreatestEnglishLetter:

    def greatestEnglishLetter(self, s):

        lower = [0 for i in range(26)]
        upper = [0 for i in range(26)]

        for i in s:
            if ord(i) >= ord('A') and ord(i) <= ord('Z'):
                upper[ord(i) - ord('A')] = 1
            else:
                lower[ord(i) - ord('a')] = 1

        answer = ""

        for i in range(26):
            if upper[i] == 1 and lower[i] == 1:
                answer = chr(ord('A') + i)

        return answer


if __name__ == "__main__":
    gel = GreatestEnglishLetter()

    s = "AbCdEfGhIjK"

    print(gel.greatestEnglishLetter(s))
