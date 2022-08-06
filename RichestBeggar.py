# your code goes here
N = int(input())
K = int(input())

# print()

queries = []

for _ in range(K):
    X = input().split(" ")

    queries.append([int(X[0])-1, int(X[1]) - 1])
arr = [0 for i in range(N)]
for query in queries:
    if 0 <= query[0] < N:
        arr[query[0]] += 1
    if query[1] + 1 < N:
        arr[query[1]] -= 1

for i in range(1, N):
    arr[i] = arr[i] + arr[i-1]

maxi = max(arr)
print(maxi)
answer = ""

for i in range(N):
    if arr[i] == maxi:
        answer += str(i + 1) + " "

print(answer[:-1])
