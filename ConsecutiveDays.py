class ConsecutiveDays:



    def consecutiveDays(self, nums):

        n = len(nums)
        i = 0

        answer = 0
        while(i < n):
            
            j = i + 1
            print(i, j)
            if nums[j] < nums[i]:
                # print(i, j)
                j += 1
            else:
                l = j - i
                answer += (l * (l + 1))// 2
                i = j

        return answer + n


if __name__ == "__main__":
    nums = [4, 3, 5, 4, 3]


    cd = ConsecutiveDays()

    print(cd.consecutiveDays(nums))