//swapping pairs in the linked list 
//ex: [1,2,3,4] should become: [2,1,4,3]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* Node=head;
    if(Node==NULL)
        return Node;
    while(Node!=NULL && Node->next!=NULL){
        int temporary_value=Node->val;
        Node->val=Node->next->val;
        Node->next->val=temporary_value;
        Node=Node->next->next;
    }
    return head;
}
//the above solution is only correct if the question is asked to modify the values in place

//but if leetcode the question is aksed to change the nodes, so the exact solution will be:
