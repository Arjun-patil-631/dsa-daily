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

//daily

#include <limits.h>

int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int ans = INT_MAX;

    for (int i = 0; i < numsSize; i++) {
        int sum = 0;

        for (int j = i; j < numsSize && j < i + r; j++) {
            sum += nums[j];

            int len = j - i + 1;

            if (len >= l && len <= r && sum > 0) {
                if (sum < ans) {
                    ans = sum;
                }
            }
        }
    }

    return ans == INT_MAX ? -1 : ans;
}
