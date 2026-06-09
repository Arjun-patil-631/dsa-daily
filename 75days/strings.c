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


  
 

