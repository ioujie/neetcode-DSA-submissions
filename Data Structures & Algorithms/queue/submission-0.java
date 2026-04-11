class LinkedNode {
    int val;
    LinkedNode next;
    
    public LinkedNode(int val) {
        this.val = val;
        this.next = null;
    }
}

class Deque {
    LinkedNode head;
    LinkedNode tail;

    public Deque() {
        this.head = new LinkedNode(-1);
        this.tail = this.head;
    }

    public boolean isEmpty() {
        if(head.next == null) {
            return true;
        } else {
            return false;
        }
    }

    public void append(int value) {
       LinkedNode newTail = new LinkedNode(value);
       tail.next = newTail;
       tail = newTail;
    }

    public void appendleft(int value) {
        LinkedNode newHead = new LinkedNode(value);
        newHead.next = head.next;
        head.next = newHead;
        if(newHead.next == null) {
            tail = newHead;
        }
    }

    public int pop() {
        if(isEmpty()) {
            return -1;
        }

        int tailVal = tail.val;

        LinkedNode cur = head;
        while(cur.next != tail) {
            cur = cur.next;
        }
        tail = cur;
        tail.next = null;

        return tailVal;
    }

    public int popleft() {
        if(isEmpty()) {
            return -1;
        }
        int headVal = head.next.val;
        if(tail == head.next) {
            tail = head;
        }
        head.next = head.next.next;
        return headVal;
    }
}
