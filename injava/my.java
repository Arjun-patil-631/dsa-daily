//06-08
//Daily question
//3345. Smallest Divisible Digit Product I
class Solution {
    public int smallestNumber(int n, int t) {
        while(true){
        int temp=n;
        int pro=1;
        while(temp>0){
            pro*=temp%10;
            temp/=10;
        }
        if(pro%t==0)
            return n;
        else
            n++;
        }
    }
}


//07-08
//majority element : which occurs more than n/2 in an array
//By boyer Moore algorithm
class Solution {
    public int majorityElement(int[] nums) {
        int element=0, count=0;
        for(int num: nums){
            if(count==0)
                element=num;
            if(num==element)
                count++;
            else
                count--;
        }
        return element;
    }
}

//09-08
//search insert
class Solution {
    public int searchInsert(int[] nums, int target) {
        int i=0, j=nums.length-1;
        int mid;
        while(i<=j){
            mid=i+(j-i)/2;
            if(nums[mid]==target)
                return mid;
            if(nums[mid]<target)
                i=mid+1;
            if(nums[mid]>target)
                j=mid-1;
        }
        return i;
    }
}

//11-08-2026
// Smallest Missing Integer Greater Than Sequential Prefix Sum
class Solution {
    public int missingInteger(int[] nums) {
        int total=nums[0];

        for(int i=1; i<nums.length; i++){
            if(nums[i]==nums[i-1]+1){
                total+=nums[i];
            }
            else{
                break;
            }
        }
        //store all numbers in a hash set
        HashSet<Integer>set=new HashSet<>();

        for(int num : nums){
            set.add(num);
        }

        //find the smallest missing integer
        while(set.contains(total)){
            total++;
        }

        return total;
    }
}