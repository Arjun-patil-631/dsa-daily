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

//17-07-2026
//reverse a linked list
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev=NULL;
    struct ListNode* curr=head;
    struct ListNode* next=NULL;
    while(curr!=NULL){
        next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=next;
    }
    return prev;
}

//04-08-2026
int maxProduct(int n) {
    int first = 0, second = 0;

    while (n > 0) {
        int digit = n % 10;

        if (digit >= first) {
            second = first;
            first = digit;
        } else if (digit > second) {
            second = digit;
        }

        n /= 10;
    }

    return first * second;
}

//05-08
//combinations LC77
int **ans;
int *returnCols;
int path[20];
int pos, count;

void backtrack(int start, int n, int k) {
    if (pos == k) {
        ans[count] = (int *)malloc(k * sizeof(int));
        for (int i = 0; i < k; i++)
            ans[count][i] = path[i];
        returnCols[count] = k;
        count++;
        return;
    }

    for (int i = start; i <= n; i++) {
        path[pos] = i;
        pos++;
        backtrack(i + 1, n, k);
        pos--;
    }
}

int combination(int n, int k) {
    if (k > n - k)
        k = n - k;

    long long res = 1;
    for (int i = 1; i <= k; i++)
        res = res * (n - k + i) / i;

    return (int)res;
}

int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {

    int total = combination(n, k);

    ans = (int **)malloc(total * sizeof(int *));
    returnCols = (int *)malloc(total * sizeof(int));

    pos = 0;
    count = 0;

    backtrack(1, n, k);

    *returnSize = count;
    *returnColumnSizes = returnCols;

    return ans;
}

//07-08-2026
//same tree

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    //if both are null
    if(p==NULL && q==NULL)
        return true;
    
    //if one is null other is not
    if(p==NULL || q==NULL)
        return false;
    
    //values are different
    if(p->val != q->val)
        return false;
    
    //check right and left subtree
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

//10-08-2026
//array partiton
int cmp(const void *a, const void *b)
{
    return (*(int *)a > *(int *)b) - (*(int *)a < *(int *)b);
}

int arrayPairSum(int* nums, int numsSize)
{
    qsort(nums, numsSize, sizeof(int), cmp);

    int sum = 0;

    for (int i = 0; i < numsSize; i += 2)
    {
        sum += nums[i];
    }

    return sum;
}
