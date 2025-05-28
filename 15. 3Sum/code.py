class Solution(object):
    def threeSum(self, nums):
        o=[];
        nums.sort();
        for i in range(len(nums)-2):
            left=i+1;
            right=len(nums)-1;
            while(left<right):
                target=-1*nums[i];
                if(nums[left]+nums[right]==target):
                    if([nums[i],nums[left],nums[right]] not in o):
                        o.append([nums[i],nums[left],nums[right]]);
                    left+=1;
                    right-=1;
                elif(nums[left]+nums[right]<target):
                    left+=1;
                else:
                    right-=1;
        return o;
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

if(__name__=="__main__"):
    nums = [-1,0,1,2,-1,-4];
    print(Solution().threeSum(nums));