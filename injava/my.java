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