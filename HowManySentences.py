class HowManySentences:

    def howManySentences(self, string, wordset):

        anagrams = {}

        for word in wordset:
            w = "".join(sorted(word))

            if w in anagrams:
                anagrams[w] += 1
            else:
                anagrams[w] = 1

        sentence = string.split(" ")

        answer = 1
        for word in sentence:
            if word in anagrams:
                answer *= anagrams[word]

        return answer


if __name__ == "__main__":
