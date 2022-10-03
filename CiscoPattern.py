def stringExpansion(string):

    stack = []

    n = len(string)

    i = 0
    while i < n:

        if string[i] != "{":
            stack.append(string[i])
            i += 1
            continue
        else:
            repeat = int(string[i + 1])

            s = ""
            k = ""
            if stack and stack[-1] == ")":
                while len(stack) > 0 and k != "(":
                    k = stack.pop(-1)

                    if k != ")" and k != "(":
                        s = k + s

                stack = stack + (list(s * repeat))

                if (i + 2 < n and string[i + 2] != "}") or i + 2 >= n:
                    return ""

            i += 3
            continue

    answer = ""

    for i in stack:
        if i != "(" and i != ")":
            answer += i

    return answer


if __name__ == "__main__":

    string = "{3}(a()){2}b({3}){3}{2}"

    print(stringExpansion(string))
