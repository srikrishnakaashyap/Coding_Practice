"""
s = "geeksforgeeks"
s = "GEEKSFORGEEKS"
"""

h = [0 for i in range(26)]

string = "geeksforgeeks"

# a -> 97
# A -> 65

# for i in s:
#     h[ord(i) - 97] += 1

# m = max(h)

# for index, value in enumerate(h):
#     if value == m:
#         print(chr(index + 97))

s = set()

answer = ""

"""
Time complexity to check if an element is present in a set/hashmap is O(1). 
"""
for i in string:
    if i not in s:
        answer += i
        s.add(i)
print(answer)
