class TextMessage:
    def text_justification(self, text, limit):
        suffix_len = 0
        text_size = len(text)
        approx = (text_size // limit) + 1

        if approx < 10:
            suffix_len = 5
        elif 10 <= approx < 100:
            suffix_len = 7
        else:
            suffix_len = 9

        if suffix_len >= limit:
            return []

        approx = (text_size // (limit - suffix_len)) + 1
        res = []
        words = text.split(" ")
        idx = 0
        for i in range(approx):
            line = ""
            while idx + 1 < len(words) and len(line + " " + words[idx]) < limit - 5:
                line += words[idx] + " "
                idx += 1
            line += "(" + str(i + 1) + "/" + str(approx) + ")"
            res.append(line)

        return res


if __name__ == "__main__":

    text = "CodeSignal"
    limit = 6

    tm = TextMessage()

    print(tm.text_justification(text, limit))
