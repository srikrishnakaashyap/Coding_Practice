class CardinalitySort:

    def cardinalitySort(self, nums):
        def f(num):
            print(bin(num))
            num_0 = bin(num)[2:].count("1")
            return num_0

        return (sorted(sorted(nums), key=f))


if __name__ == "__main__":
    cs = CardinalitySort()

    nums = [1, 2, 3, 4]
    print(cs.cardinalitySort(nums))
