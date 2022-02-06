def twosum(arr, target):
    temp = dict()

    for i in arr:
        temp[i] = 1
    
    for i in arr:
        if (target - i) in temp:
            return [i, target-i]
    
    return 'Not Available'
    


if __name__ == "__main__":

    arr = [4,5,6,7,89]
    target = 13

    print(twosum(arr, target))
