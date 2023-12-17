class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *p1 = l1, 2 = l2;
        while(p1 != NULL || p2 != NULL){
            if(p1 == NULL){
                ListNode *newNode = new ListNode(0);//Adding 0's to end of the first list if its size is less than second list
                newNode->next = l1;
                l1 = newNode;
                
                p2 = p2->next;
            }
            else if(p2 == NULL){
                ListNode *newNode = new ListNode(0); //Adding 0's to end of the second list if its size is less than first list
                newNode->next = l2;
                l2 = newNode;
                p1 = p1->next;
            }
            else{
                p1 = p1->next;
                p2 = p2->next;
            }
        }
        int carry = 0;
        ListNode *dummy = new ListNode(-1);
        dummy->next = addTwoDigit(l1, l2, carry);
        if(carry != 0){
            ListNode *newNode = new ListNode(carry);
            newNode->next = dummy->next;
            dummy->next = newNode;
        }
        return dummy->next;
    }
    ListNode* addTwoDigit(ListNode* l1, ListNode* l2, int &carry){ //recursion is used to perform addition 
        if(l1 == NULL && l2 == NULL)  return NULL;
        ListNode *newNode = new ListNode(-1);
        newNode->next = addTwoDigit(l1->next, l2->next, carry);
        newNode->val = (l1->val + l2->val + carry) % 10;
        carry = (l1->val + l2->val + carry) / 10;
        return newNode;
    }
};