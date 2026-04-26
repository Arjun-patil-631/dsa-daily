int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
   *returnSize=2;

// Allocate memory for the result array to hold the indices 
// of the two numbers that add up to the target
int* result=(int*)malloc(*returnSize * sizeof(int));

// Iterate through the array to find the two numbers that add up to the target
for(int i=0; i<numsSize; i++){
 for(int j = i + 1; j < numsSize; j++) {
            if(nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result; //return indices of the two numbers
            }
        }
    }
    *returnSize = 0;//if no solution is found, set returnSize to 0
    return NULL; //return NULL if no solution is found
}
 