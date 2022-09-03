class TripletsCount:



    def tripletsCount(self, arr):
        
        bval = 0
        bIndex = -1

        n = len(arr)
 
        # Iterate for middle element
        for j in range(1, n - 1):
            p, q = 0, 0
    
            # Iterate left array for a[i]
            for i in range(j):
    
                if (arr[j] % arr[i] == 0):
                    p += 1
    
            # Iterate right array for a[k]
            for k in range(j + 1, n):
    
                if (arr[k] % arr[j] == 0):
                    q += 1
    
            count += p * q
            
        # Return the final result
        return count


if __name__ == "__main__":

    tc = TripletsCount()

