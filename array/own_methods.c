//moving zeroes to the end of the array
void moveZeroes(int* nums, int numsSize) {
    int *i=nums, *j=nums+1;
    while(j<nums+numsSize){
        if(*i==0 && *j!=0){
            *i=*j;
            *j=0;
        }
        else if(*i==0 && *j==0){
            j++;
        }
        else {
            i++;
            j++;
        }
    }
}