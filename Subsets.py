def SubsetHelper(array, index, current, ans):

    if(index == len(array)):
        return current

    ans.append(SubsetHelper(array, index+1, current[:], ans))
    current.append(array[index])
    ans.append(SubsetHelper(array, index+1, current[:], ans))

    return ans


if __name__ == "__main__":
    array = [1, 2, 3]

    print(SubsetHelper(array, 0, [], []))
