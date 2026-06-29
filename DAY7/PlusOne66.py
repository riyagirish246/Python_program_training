class solution:
    def Plusone(num):
        n=len(num)-1
        for i in range(n,-1,-1):
            if num[i]<9:
                num[i]+=1
                return num
            nums[i]=0
        result=[0]*(len(num)+1)
        result[0]=1
        return result
