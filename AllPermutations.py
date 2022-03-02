class AllPermutations:

    def all_permutations(array):
        ans = []

        n = len(array)
        m = [0 for i in range(n)]

        def print_all_permutations(m, arr):
            if len(arr) == n:
                ans.append(arr[:])
                return

            for i in range(0, n):
                # for j in range(len(m)):
                if(m[i] == 0):
                    m[i] = 1
                    arr.append(array[i])
                    print_all_permutations(m, arr)
                    m[i] = 0
                    arr.pop()
                    # print_all_permutations(i + 1, m, arr)

        print_all_permutations(m, [])
        return ans

    if __name__ == "__main__":

        array = [1, 2, 3]

        print(all_permutations(array))
