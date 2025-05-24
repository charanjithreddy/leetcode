class Solution(object):
    def triangleType(self, nums):
        if(nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[2]+nums[0]>nums[1]):
            if(nums[0]==nums[1] and nums[1]==nums[2]):
                return "equilateral";
            elif(nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]):
                return "isosceles";
            else:
                return "scalene";
        else:
            return "none";
        """
        :type nums: List[int]
        :rtype: str
        """

if(__name__=="__main__"):
    nums = [3,3,3];

    print(Solution().triangleType(nums));