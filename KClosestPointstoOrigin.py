class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin=[0,0]
        result=[]
        newresult=[]
        output=[]

        for i in range(0, len(points)):
            n=points[i][0]-origin[0]
            m=points[i][1]-origin[1]
            z=n**2 + m**2
            result.append(z)


        #return k number of smallest points
        newresult=result.copy()
        for j in range (0,k):
            if(len(output)>=k):
                j=k
            else:
                #get minimum sqrt
                a= min(newresult)
                #return point with min distance
                for x in range(0,len(result)):
                    if(result[x]==a):
                        output.append(points[x])
                newresult.remove(a)  

        return output
