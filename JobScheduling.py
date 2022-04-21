class JobScheduling:

    def jobScheduling(self, jobs):

        jobs = sorted(jobs, key=lambda x: x[1], reverse=True)

        # m = max(m, jobs lambda x: x[0])
        m = 0

        for j in jobs:
            m = max(m, j[0])

        print(m)

        values = [0 for i in range(m + 1)]
        print(len(values))
        ctr = 0
        n = len(jobs)
        profit = 0
        while(ctr < n):
            index = jobs[ctr][0]

            print(index)

            while index >= 0 and values[index] != 0:
                index -= 1

            if index > 0 and values[index] == 0:
                values[index] = jobs[ctr][1]

            ctr += 1

        return sum(values)


if __name__ == "__main__":
    js = JobScheduling()

# 2 4 1 3 5
# 25 40 5 50 60
    # arr = [[2, 25], [4, 40], [1, 5], [3, 50], [5, 60]]
    # arr = [[2, 40], [2, 20], [2, 10]]
    arr = [[2, 30], [2, 40], [1, 10], [1, 10]]

    print(js.jobScheduling(arr))
