from tkinter import N


class NthRoot:

    def multiply(self, mid, n):
        answer = 1.0
        for i in range(n):
            answer *= mid

        return answer

    def nthRoot(self, m, n):
        low = 1
        high = n

        while(high - low) > 0.0000001:
            mid = (low + (high - low)/2)

            # print(mid)

            if self.multiply(mid, m) < n:
                low = mid
            else:
                high = mid

        return low


if __name__ == "__main__":
    nr = NthRoot()
    m = 4
    n = 69

    print(nr.nthRoot(m, n))
