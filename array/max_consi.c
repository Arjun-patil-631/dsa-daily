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

//daily 16-11-26
//digit sum of a string
char* digitSum(char* s, int k) {
    while (strlen(s) > k) {
        char* result = malloc(strlen(s) * 4 + 1);
        int pos = 0;

        for (int i = 0; i < strlen(s); i += k) {
            int sum = 0;

            for (int j = i; j < i + k && s[j] != '\0'; j++) {
                sum += s[j] - '0';
            }

            pos += sprintf(result + pos, "%d", sum);
        }

        result[pos] = '\0';
        s = result;
    }

    return s;
}