class FractionalKnapsack:

    def fractionalKnapsack(self, weights, values, w):

        pairs = []
        n = len(weights)
        for i in range(n):
            temp = [weights[i], values[i], values[i]/weights[i]]
            pairs.append(temp)

        items = pairs

        print(items)
        # for i in range(n):
        #     temp = items[i][1] / items[i][0]
        #     items[i].append(temp)

        items = sorted(items, key=lambda x: x[2], reverse=True)

        print(items)
        ctr = 0
        m = 0
        while(w > 0):
            t = min(w, items[ctr][0])
            print(t)
            # print
            val = items[ctr][1] if t == items[ctr][0] else t * items[ctr][2]
            m += val
            w -= t
            ctr += 1

        return m


if __name__ == "__main__":

    fk = FractionalKnapsack()

    weights = [50, 40, 90, 120, 10, 200]
    values = [40, 50, 25, 100, 30, 45]

    w = 200

    print(fk.fractionalKnapsack(weights, values, w))
