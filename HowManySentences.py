class HowManySentences:
    def howManySentences(self, sentences, wordset):

        anagrams = {}

        for word in wordset:
            w = "".join(sorted(word))

            if w in anagrams:
                anagrams[w] += 1
            else:
                anagrams[w] = 1

        # print(anagrams)

        answer = []
        for s in sentences:
            sentence = s.split(" ")
            t = 1
            for word in sentence:
                if "".join(sorted(word)) in anagrams:
                    t *= anagrams["".join(sorted(word))]

            answer.append(t)

        return answer


if __name__ == "__main__":
    wordset = ["the", "bats", "tabs", "in", "cat", "act"]
    sentence = ["cat the bats", "in the act", "act tabs in"]

    hm = HowManySentences()

    print(hm.howManySentences(sentence, wordset))
