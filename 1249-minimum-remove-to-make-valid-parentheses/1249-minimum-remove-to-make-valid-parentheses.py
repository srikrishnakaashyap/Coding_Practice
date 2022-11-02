class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        inp = []
        output = []

        for c in s:
            inp.append(c)

        for i in range(len(inp)):
            if inp[i] == '(':
                stack.append(i)
            elif inp[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    inp[i] = '*'

        for i in range(len(stack)):
            inp[stack[i]] = '*'

        for i in range(len(inp)):
            if inp[i] != '*':
                output.append(inp[i])

        return "".join(output)
