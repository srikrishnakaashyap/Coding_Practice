class NextGreaterElement:

    def nextGreaterElement(self, nums1, nums2):

        stack = []
        n = len(nums2)
        m = len(nums1)
        ngemap = {}
        answer = []
        for i in range(n-1, -1, -1):

            while(len(stack) > 0 and stack[-1] <= nums2[i]):
                stack.pop()

            if len(stack) > 0:
                ngemap[nums2[i]] = stack[-1]
            else:
                ngemap[nums2[i]] = -1

            stack.append(nums2[i])

        for i in range(m):
            answer.append(ngemap[nums1[i]])

        return answer


if __name__ == "__main__":

    nge = NextGreaterElement()

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    print(nge.nextGreaterElement(nums1, nums2))
