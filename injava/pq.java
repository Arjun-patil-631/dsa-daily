//17-08-2026
//Move Zeroes
class Solution {
    public void moveZeroes(int[] nums) {
        int i=0, j=1,temp;
        while(j<nums.length){
            if(nums[i]==0 && nums[j]!=0){
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                i++;
                j++;
            }
            else if(nums[i]==0 && nums[j]==0){
                j++;
            }
            else{
                i++;
                j++;
            }
        }
    }
}