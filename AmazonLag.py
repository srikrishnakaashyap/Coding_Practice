class AmazonLag:


    def amazonLag(self, center, destination):

        center = sorted(center)
        destination = sorted(destination)
        answer = 0

        for i in range(len(center)):
            answer += abs(center[i] - destination[i])
        
        return answer

    
    

if __name__ == "__main__":
    al = AmazonLag()

    center = 

