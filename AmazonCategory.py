class AmazonCategory:
    def category(self, string):

        prefix = [{} for i in range(len(string))]

        tmp = {}
        tmp[string[0]] = 1
        prefix[0] = tmp
        for i, j in enumerate(string):
            if i > 0:
                tmp = prefix[i - 1].copy()
                if j in tmp:
                    tmp[j] += 1
                else:
                    tmp[j] = 1

                prefix[i] = tmp

        hm = {}

        for dictionary in prefix:
            m = max(dictionary.values())

            for key, value in dictionary.items():
                if value == m:

                    if key in hm:
                        hm[key] += 1
                    else:
                        hm[key] = 1

        return max(hm.values())


if __name__ == "__main__":
    ac = AmazonCategory()

    string = "bccaaacb"

    print(ac.category(string))
