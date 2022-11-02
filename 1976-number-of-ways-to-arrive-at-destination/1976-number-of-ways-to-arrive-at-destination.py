import heapq
import math
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = [[] for i in range(n)]
        
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))
            
        pq = []
        
        distance = [math.inf for i in range(n)]
        ways = [0 for i in range(n)]
        
        distance[0] = 0
        ways[0] = 1
        pq.append((0, 0))
        
        while(pq):
            elem = heapq.heappop(pq)
            
            dist = elem[0]
            node = elem[1]
            
            for a in adj[node]:
                if dist + a[1] < distance[a[0]]:
                    distance[a[0]] = dist + a[1]
                    ways[a[0]] = ways[node]
                    heapq.heappush(pq, (distance[a[0]], a[0]))
                
                elif dist + a[1] == distance[a[0]]:
                    ways[a[0]] = ways[a[0]] + ways[node]
        
        # pri
        answer = ways[n-1]
        # print(answer)
        answer = answer % ((10**9) + 7)
        return answer
        # return ways[n-1] % (10**9) + 7
                    
        