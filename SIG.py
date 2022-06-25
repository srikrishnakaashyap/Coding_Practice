class SIG:

    def sig(self, words):
        d = []

        answer = 0

        for word in words:
            sorted_word = "".join(sorted(word))

            # binary_search(sorted_word, d)

            if sorted_word in d:
                d[sorted_word] += 1
            else:
                d[sorted_word] = 1
                answer += 1

        return answer


if __name__ == "__main__":

    s = SIG()

    words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]

    print(s.sig(words))
