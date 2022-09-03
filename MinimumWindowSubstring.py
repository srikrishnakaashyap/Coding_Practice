from collections import defaultdict


class MinimumWindowSubstring:
    def check_window(self, current, final):

        # print(current, final)

        for key, value in final.items():
            if key not in current or current[key] < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        if s == t:
            return s

        chars_to_find = defaultdict(int)

        for c in t:
            chars_to_find[c] += 1

        current = defaultdict(int)

        low = 0
        high = 1
        n = len(s)
        minWindow = n + 1
        current[s[low]] += 1

        answer = ""

        n = len(s)
        while low < n and high < n:

            # print(current)

            if not self.check_window(current, chars_to_find):
                current[s[high]] += 1
                high += 1
            else:
                # print(current, low, high)

                if high - low < minWindow:

                    minWindow = high - low
                    answer = s[low:high]
                current[s[low]] -= 1
                low += 1

        print(current, low, high)
        while low < n:
            if self.check_window(current, chars_to_find):
                # print(low, current)
                if high - low < minWindow:
                    minWindow = high - low
                    answer = s[low:high]
                current[s[low]] -= 1
                low += 1
            else:
                break

        return answer


if __name__ == "__main__":

    ms = MinimumWindowSubstring()

    s = "abc"
    t = "ac"

    print(ms.minWindow(s, t))
