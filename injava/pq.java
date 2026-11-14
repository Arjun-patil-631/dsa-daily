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

//Longest Strictly Increasing or Strictly Decreasing Subarray
class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int inc = 1;
        int dec = 1;
        int ans = 1;

        for (int i = 1; i < nums.length; i++) {

            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            }
            else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            }
            else {
                inc = 1;
                dec = 1;
            }

            ans = Math.max(ans, Math.max(inc, dec));
        }

        return ans;
    }
}

//minimum sum subarray
class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int n = nums.size();
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int sum = 0;

            for (int j = i; j < Math.min(n, i + r); j++) {
                sum += nums.get(j);

                int len = j - i + 1;

                if (len >= l && len <= r && sum > 0) {
                    ans = Math.min(ans, sum);
                }
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
