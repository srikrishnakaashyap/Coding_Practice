class CommonStrings:


    def commonStrings(self, categories, k):
        
        categories = list(categories)
        n = len(categories)
        prefix = [0 for i in range(n)]
        s = set()
        s.add(categories[0])
        prefix[0] = s.copy()

        for i in range(1, n):
            s.add(categories[i])
            prefix[i] = s.copy()


        suffix = [0 for i in range(n)]
        s = set()

        for i in range(n-2, -1, -1):
            s.add(categories[i + 1])
            suffix[i] = s.copy()
            
        answer = 0

        for i in range(n - 1):

            s1 = prefix[i]
            s2 = suffix[i]
            cnt = 0

            for j in s1:
                if j in s2:
                    cnt += 1
            if cnt > k:
                answer += 1
        
        return answer


    def commonStrings2(self, categories, k):

        categories = list(categories)
        n = len(categories)
        prefix = [0 for i in range(n)]
        s = set()
        s.add(categories[0])
        prefix[0] = s.copy()

        for i in range(1, n):
            s.add(categories[i])
            prefix[i] = s.copy()
        
        s = set()

        answer = 0
        for i in range(n-2, -1, -1):

            s.add(categories[i+1])

            s1 = prefix[i]
            cnt = 0
            for j in s1:
                if j in s:
                    cnt += 1
            if cnt > k:
                answer += 1
        
        return answer



if __name__ == "__main__":

    cs = CommonStrings()

    categories = "adbccdbada"
    k = 2

    print(cs.commonStrings2(categories, k))