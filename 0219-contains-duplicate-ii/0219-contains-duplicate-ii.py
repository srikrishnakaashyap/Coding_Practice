class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         i = 0
        
#         n = len(nums)
        
#         while(i < n):
#             j = i + 1
#             while(abs(i - j) <= k):
#                 if nums[i] == nums[j]:
#                     return True
#                 j += 1
#             i = j
        
#         return False

# O(n) time and space
#         {
#             1: [0, 3]
#             2: [1]
#             3: [2]
            
#         }

        hm = {}
    
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]].append(i)
            else:
                hm[nums[i]] = [i]
        
        for key, values in hm.items():
            
            n = len(values)
            for i in range(1, n):
                if abs(values[i] - values[i-1]) <= k:
                    return True
        
        return False
        