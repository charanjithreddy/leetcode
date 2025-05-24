class Solution(object):
    def isZeroArray(self, nums, queries):
        if(max(nums)>len(queries)):
            return False;
        d=[0]*(len(nums));
        for [x,y] in queries:
            d[x]+=1;
            if(y<len(nums)-1):
                d[y+1]-=1;
        if(nums[0]>d[0]):
            return False;
        for i in range(1,len(nums)):
            d[i]+=d[i-1];
            if(nums[i]>d[i]):
                return False;
        return True;
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """

if(__name__=="__main__"):
    nums = [1,0,1];
    queries = [[0,2]];

    print("Output:");
    print(Solution().isZeroArray(nums,queries));