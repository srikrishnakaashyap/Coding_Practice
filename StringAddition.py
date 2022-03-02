def StringAddition(string):

    start = 0
    end = len(string) - 1

    answer = ""
    while(start < end):
        ans = int(string[start]) + int(string[end])

        answer += str(ans)
        start += 1
        end -= 1

    if(len(string) % 2 == 1):
        answer += string[start]

    return answer


if __name__ == "__main__":

    print(StringAddition("434256"))
    print(StringAddition("4342565"))
