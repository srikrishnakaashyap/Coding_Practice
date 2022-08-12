class TwoSum2:



    def twoSum2(self, numbers, target):

        answer = [-1, -1]

        n = len(numbers)
        for i, j in enumerate(numbers):
            # print(i, j)

            remaining = target - j

            low = i + 1
            high = n - 1

            while(low <= high):
                mid = (low + high) // 2
                if numbers[mid] == remaining:
                    answer[0] = i + 1
                    answer[1] = mid + 1
                    break
                if numbers[mid] < remaining:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return answer


        


if __name__ == "__main__":

    ts = TwoSum2()

    numbers = [2,7,11,15]
    target = 9

    print(ts.twoSum2(numbers, target))