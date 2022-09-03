class KConsistency:
    def kConsistency(self, nums, k):

        hm = {}
        for i, j in enumerate(nums):
            if j in hm:
                hm[j].append(i)
            else:
                hm[j] = [i]
        answer = 0
        for key, values in hm.items():

            if len(values) < answer:
                continue

            localAns = 0
            j = 0
            k = 1
            subs = 0
            while k < len(values):
                pass

            answer = max(answer, localAns)
        return answer

    def KConsistencyUday(self, nums, k):
        store = dict()
        for i in range(len(nums)):
            if nums[i] not in store:
                store[nums[i]] = [i]
            else:
                store[nums[i]].append(i)

        ans = 1
        lst_set = set(nums)

        def slide(index_list):

            # print(index_list)
            temp = 0
            curr = 0

            for i in range(1, len(index_list)):
                # print("In the for loop")
                curr += index_list[i] - index_list[i - 1] - 1

                while curr > k:
                    temp += 1
                    curr -= index_list[temp] - index_list[temp - 1] - 1
                nonlocal ans
                ans = max(ans, i - temp + 1)

        for value in store.values():
            slide(value)

        return ans


if __name__ == "__main__":

    kc = KConsistency()

    nums = [7, 5, 7, 7, 1, 1, 7, 7]
    k = 3

    print(kc.KConsistencyUday(nums, k))
