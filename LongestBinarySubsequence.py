class LongestBinarySubsequence:

    def longestSubsequence(self, s, k):

        b = 1
        value = 0

        n = len(s)
        answer = 0

        for i in range(n-1, -1, -1):
            if s[i] == '1':
                if value + b <= k:
                    answer += 1
                    value += b
                    # b *= 2
            else:
                answer += 1

            b *= 2

        return answer


if __name__ == "__main__":

    lbs = LongestBinarySubsequence()

    s = "001010010"
    k = 1

    print(lbs.longestSubsequence(s, k))
