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

//merging two sorted lists
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

    struct ListNode dummy;
    struct ListNode *temp = &dummy;

    dummy.next = NULL;

    while(list1 != NULL && list2 != NULL) {

        if(list1->val <= list2->val) {
            temp->next = list1;
            list1 = list1->next;
        }
        else {
            temp->next = list2;
            list2 = list2->next;
        }

        temp = temp->next;
    }

    // attach remaining nodes
    if(list1 != NULL)
        temp->next = list1;
    else
        temp->next = list2;

    return dummy.next;
        
    }
};

//23-05-2026//
//add 2 numbers represented as linked lists
/**
 * Definition for singly-linked list*/.
 struct ListNode {
      int val;
     struct ListNode *next;
 };

struct ListNode* createNode(int val){
    struct ListNode* newNode=(struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val=val;
    newNode->next=NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    dummy.next=NULL;

    struct ListNode* temp= &dummy;
    int carry=0;

    while(l1!=NULL || l2!=NULL || carry!=0){
        int sum=carry;

        if(l1!=NULL){
            sum+=l1->val;
            l1=l1->next;
        }
        if(l2!=NULL){
            sum+=l2->val;
            l2=l2->next;
        }
        carry=sum/10;
        struct ListNode* newNode=createNode(sum%10);
        temp->next=newNode;
        temp=temp->next;
    }
    return dummy.next;
}

/*
#29-06-2026
#no of strings that appers as substring in a given string*/
int numOfStrings(char** patterns, int patternsSize, char* word) {
    int count=0;
    for(int i=0; i<patternsSize; i++){
        if(strstr(word, patterns[i])!=NULL)
            count++;
    }
    return count;
}