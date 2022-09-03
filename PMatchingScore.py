from re import L


class PMatchingScore:

    def checkHashes(self, h1, h2):
        for i in range(26):
            if h1[i] != h2[i]:
                return False
        
        return True
                
    def pMatchingScore(self, string1, string2, p):

        m = len(string1)
        n = len(string2)

        ans = 0

        compareHash = [0 for i in range(26)]

        for i in string2:
            compareHash[ord(i) - 97] += 1


        hm = [[0 for i in range(26)] for j in range(p)]

        # print(len(hm))

        for i in range(0, p):
            temp = ""

            j = i
            while len(temp) < n and j < m:
                temp += string1[j]
                hm[i][ord(string1[i]) - 97] += 1
                j += p

            if self.checkHashes(hm[i], compareHash):
                ans += 1

            if len(temp) < n:
                broken = True
                break
        
        if broken:
            return ans

        for i in range(p, m):
            j = i + (n - 1) * p
            toRemove = i - (n-1) * p
            if j < m:
            else:
                break
            toRemoveIndex = i - 

        return ans

    def pMatchingScore2(self, string1, string2, p):

        n = len(string1)
        m = len(string2)
        answer = 0


if __name__ == "__main__":
    pms = PMatchingScore()

    string1 = "abcbcdcadbb"
    string2 = "ab"
    p = 2

    print(pms.pMatchingScore(string1, string2, p))
