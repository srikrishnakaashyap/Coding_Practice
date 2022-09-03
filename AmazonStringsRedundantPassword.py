from multiprocessing.connection import answer_challenge


class AmazonStringsRedundantPassword:
    def redundant(self, string):
        hm = {}
        answer = 1
        for i in string:
            print(hm)
            if i not in hm:
                hm[i] = 1
            else:
                hm = {}
                hm[i] = 1
                answer += 1

        return answer


if __name__ == "__main__":
    asr = AmazonStringsRedundantPassword()

    string = "alabama"

    print(asr.redundant(string))
