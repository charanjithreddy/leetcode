#include<stdio.h>

char* triangleType(int* nums, int numsSize) {
    if(nums[0]+nums[1]>nums[2] && nums[1]+nums[2]>nums[0] && nums[2]+nums[0]>nums[1]){
        if(nums[1]==nums[2] && nums[0]==nums[1]){
            return "equilateral";
        }
        else if(nums[0]==nums[1] ||nums[1]==nums[2]||nums[2]==nums[0]){
            return "isosceles";
        }
        else{
            return "scalene";
        }
    }
    else{
        return "none";
    }
}
int main(){
    int nums[] = {3,3,3};
    printf("%s\n", triangleType(nums, sizeof(nums)/sizeof(nums[0])));
    return 0;
}