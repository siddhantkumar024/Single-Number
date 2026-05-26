class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        c=0
        for i in nums:
            if i in dic:
                c+=1
                dic[i]=c
            else:
                c=1
                dic[i]=c
        for i,c in dic.items():
            if dic[i]==1:
                return i
        
