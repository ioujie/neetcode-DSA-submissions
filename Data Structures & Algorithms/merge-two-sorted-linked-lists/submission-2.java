/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null) {
            return list2;
        } else if(list2 == null) {
            return list1;
        }

        ListNode ansHead, ansCur, insHead, insCur, head;
        if(list1.val <= list2.val) {
            ansHead = list1;
            insHead = list2;
        } else {
            ansHead = list2;
            insHead = list1;
        }
        head = ansHead;
        ansCur = ansHead;
        insCur = insHead;
        while(ansCur.next != null) {
            if(ansCur.next.val < insCur.val) {
                ansCur = ansCur.next;
                ansHead = ansHead.next;
                continue;
            }
            while(insCur.next != null && insCur.next.val <= ansCur.next.val) {
                insCur = insCur.next;
            }
            ansCur = ansCur.next;
            ansHead.next = insHead;
            insHead = insCur.next;
            insCur.next = ansCur;
            insCur = insHead;
            ansHead = ansCur;
            if(insCur == null) {
                break;
            }
        }
        if(ansCur.next == null && insCur != null) {
            ansCur.next = insCur;
        }
        return head;
    }
}