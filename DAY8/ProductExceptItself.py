class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length
       
        prefix = 1  #Prefix Products
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
           
        suffix = 1  # Suffix Products
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
           
        return answer






def productExceptSelf(nums):
    n=len(nums)
    answer=[1]*n
    prefix=1
    for i in range(n):
        answer[i]=prefix
        prefix=prefix*nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        answer[i]=answer[i]*suffix
        suffix=suffix*nums[i]
    return answer
nums=[1,2,3,4]
print(productExceptSelf(nums))
