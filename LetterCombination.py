class LetterCombination:

    def letterCombination(self, digits):

        answer = []

        keys = ["", "", "abc", "def", "ghi",
                "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def solve(index, comb):

            if index >= len(digits):
                answer.append(comb)
                return

            for ch in list(keys[int(digits[index])]):
                comb = comb + ch
                solve(index + 1, comb)
                comb = comb[:index] + comb[index+1:]

        solve(0, "")

        return answer


if __name__ == "__main__":

    digits = "23"

    answer = LetterCombination().letterCombination(digits)

    print(answer)
