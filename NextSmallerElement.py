class NextSmallerElement:

    def nextSmallerElement(self, arr):

        answer = [-1 for i in range(len(arr))]

        stack = []

        for i in range(len(arr)):
            while(len(stack) > 0 and stack[-1] > arr[i]):
                stack.pop()

            if len(stack) > 0:
                answer[i] = stack[-1]
            else:
                answer[i] = -1

            stack.append(arr[i])

        return answer


if __name__ == "__main__":

    nse = NextSmallerElement()

    arr = [4, 5, 2, 10, 8]

    print(nse.nextSmallerElement(arr))
