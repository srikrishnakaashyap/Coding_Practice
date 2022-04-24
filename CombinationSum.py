class CombinationSum:

    def combinationSum(self, candidates, target):

        candidates = sorted(candidates)
        n = len(candidates)
        ans = []
        array = []
        s = 0

        def getComb(index, array, s, target):

            if target == 0:
                ans.append(array.copy())
                return

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break

                array.append(candidates[i])
                getComb(i+1, array, s, target - candidates[i])
                array.pop()

        getComb(0, array, 0, target)

        return ans


if __name__ == "__main__":
    cs = CombinationSum()

    array = [2, 3, 6, 7]
    target = 7
    print(cs.combinationSum(array, target))
