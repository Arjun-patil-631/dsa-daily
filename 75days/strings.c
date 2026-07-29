//revere vowels in a string
char* reverseVowels(char* s) {
    int left=0, right=strlen(s)-1;
    while(left<right){
        while(left<right && !(s[left]=='a' || s[left]=='e' || s[left]=='i' || s[left]=='o' || s[left]=='u' ||
            s[left]=='A' || s[left]=='E' || s[left]=='I' || s[left]=='O' || s[left]=='U' )){
                left++;
            }
        while(left<right && !(s[right]=='a' || s[right]=='e' || s[right]=='i' || s[right]=='o' || s[right]=='u' ||
            s[right]=='A' || s[right]=='E' || s[right]=='I' || s[right]=='O' || s[right]=='U')){
                right--;
            }
        if(left<right){
            char temp=s[left];
            s[left]=s[right];
            s[right]=temp;

            left++;
            right--;
        }
    }
    return s;
}


  
//29-07-2026
#include<limits.h>
int myAtoi(char* s) {
    long result = 0;
    int sign = 1;

    while (*s == ' ')
        s++;

    if (*s == '+' || *s == '-') {
        if (*s == '-')
            sign = -1;
        s++;
    }

    while (*s >= '0' && *s <= '9') {
        result = result * 10 + (*s - '0');

        if (sign * result > INT_MAX)
            return INT_MAX;
        if (sign * result < INT_MIN)
            return INT_MIN;

        s++;
    }

    return (int)(sign * result);
}
 

