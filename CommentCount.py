class CommentCount:
    def solution(source):
        curr, ans = [], 0
        for s in source:
            temp_ans = 0
            for i in range(len(s)):
                if s[i] == " ":
                    continue
                elif not curr and s[i] == "/" and i + 1 < len(s) and s[i + 1] == "/":
                    break
                elif not curr and s[i] == "/" and i + 1 < len(s) and s[i + 1] == "*":
                    curr.append("/*")
                    i += 1
                    continue
                elif curr and s[i] != "*":
                    continue
                elif curr and s[i] == "*" and i + 1 < len(s) and s[i + 1] == "/":
                    curr.pop()
                    i += 1
                    continue
                else:
                    temp_ans += 1
            ans += temp_ans
        return ans


if __name__ == "__main__":

    cc = CommentCount()

    source = source = [
        "return a / b * c/a / b / c*/;",
    ]

    print(cc.commentCount(source))
