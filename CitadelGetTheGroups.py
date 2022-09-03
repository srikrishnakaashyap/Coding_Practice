from collections import defaultdict


class GetTheGroups:
    def groups(self, queryType, student1, student2):

        hm = defaultdict(set)

        n = len(queryType)

        for i in range(n):

            if queryType[i] == "Friend":
                pass
            else:
                pass


if __name__ == "__main__":

    g = GetTheGroups()

    queryType = ["Friend", "Friend", "Total"]

    student1 = [1, 2, 1]
    student2 = [2, 3, 4]

    print(g.groups(queryType, student1, student2))
