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
