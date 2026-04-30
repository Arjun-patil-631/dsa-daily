void sortColors(int* nums, int numsSize) {
    int count0, count1, count2, i;
    count0=count1=count2=0;
    for(i=0; i<numsSize; i++){
        if(nums[i]==0) count0++;
        else if(nums[i]==1) count1++;
        else count2++;
    }
    for(i=0; i<count0; i++)
        nums[i]=0;
    for(i=count0; i<count0+count1; i++)
        nums[i]=1;
    for(i=count0+count1; i<count0+count1+count2; i++)
        nums[i]=2;
}

}