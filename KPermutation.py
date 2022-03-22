class KPermutation:

    def kpermutation(self, n, k):

        numbers = []
        fact = 1
        for i in range(1, n):
            fact = fact * i
            numbers.append(i)
        numbers.append(n)

        answer = ""
        k -= 1
        while(True):
            answer += numbers[k//fact]
            numbers.pop(k//fact)
            if(len(numbers) == 0):
                break
            k = k % fact
            fact = fact // len(numbers)

        return answer


if __name__ == "__main__":

    n = 3
    k = 3

    print(KPermutation().kpermutation(n, k))
