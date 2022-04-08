class Container:

    def container(self, height):

        n = len(height)
        # left = [0 for i in range(n)]

        # left[0] = height[0]
        # for i in range(1, n):
        #     left[i] = max(left[i - 1], height[i])

        # left[n - 1] = min(left[n-1], height[n - 1])
        # for i in range(n-2, -1, -1):
        #     left[i] = min(left[i], height[i])

        i = 0
        j = n - 1
        m = 0
        while(i < j):
            temp = min(height[i], height[j]) * (j - i)
            m = max(m, temp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return m


if __name__ == "__main__":

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    c = Container()

    print(c.container(height))
