

def permutations_helper(array):

    def permutations(first, curr):

        if(len(curr) == 3):
            output.append(curr)
            return

        for index in range(first, len(array)):

            curr.append(array[index])

            permutations(index+1, curr)

            curr.pop()

            permutations(index + 1, curr)

    output = []

    # for k in range(len(array) + 1):
    permutations(0, [])

    return output


if __name__ == "__main__":

    array = [1, 2, 3]

    print(permutations_helper(array))
