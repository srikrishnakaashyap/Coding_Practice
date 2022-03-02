

def permutations_helper(array):

    def permutations(first=0, curr=[]):

        if(len(curr) == k):
            output.append(curr[:])
            return

        for index in range(first, len(array)):

            curr.append(array[index])

            permutations(index+1, curr)

            curr.pop()

    output = []

    for k in range(len(array) + 1):
        permutations()

    return output


if __name__ == "__main__":

    array = [1, 2, 3]

    print(permutations_helper(array))
