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
