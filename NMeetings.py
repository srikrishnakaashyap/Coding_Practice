class NMeetings:

    def nMeetings(self, start, end):

        n = len(start)
        pairs = []

        for i in range(n):
            pairs.append([start[i], end[i]])

        # pairs = sorted(pairs, key=lambda x: x[0])

        ctr = 0
        curr = []
        print(pairs)
        for i in range(len(pairs)):
            if not curr:
                curr = pairs[i]
                ctr += 1
            else:
                if pairs[i][0] > curr[1]:
                    ctr += 1
                    curr = pairs[i]

        return ctr


if __name__ == "__main__":

    nm = NMeetings()

    start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]

    end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]

    print(nm.nMeetings(start, end))
