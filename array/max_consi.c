int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int count=0, max=0;
    for(int i=0; i<numsSize; i++){
        if(nums[i]==1) count++;
        else {
            max=(count>max)?  count : max;
            count=0;
        }
    }
    if(count>=max)
        return count;
    else return max;
}