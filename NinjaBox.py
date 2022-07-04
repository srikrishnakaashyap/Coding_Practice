class NinjaBox:

    def ninjaTruck(self, box, k):

        box = sorted(box, key=lambda x: x[1], reverse=True)

        print(box)
        answer = 0
        ctr = 0
        while k > 0 and ctr < len(box):
            curr = min(k, box[ctr][0])
            answer += curr * box[ctr][1]
            k -= curr
            ctr += 1

        return answer


if __name__ == "__main__":

    nb = NinjaBox()

    box = [[1, 1], [2, 5], [1, 3]]
    k = 3

    print(nb.ninjaTruck(box, k))
