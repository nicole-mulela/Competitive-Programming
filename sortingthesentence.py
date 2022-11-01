class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        sort=[]
        #my_str =  "abcdefghij"
        #my_str = my_str[:-1]
        #rearange order
        #fetch last element
        for i in range(len(arr)):
            word=arr[i]
            sort.append(word[-1])
        #split last element
        for e in range(len(arr)):
            a=arr[e]
            arr[e]=a[:-1]
        #rearange last element and words
        for j in range(len(arr)-1):
            for x in range(j+1,len(arr)):
                if(sort[j]>sort[x]):
                    sort[j],sort[x]=sort[x],sort[j]
                    arr[j],arr[x]=arr[x],arr[j]

        result=" ".join(map(str,arr))
        return(result)
