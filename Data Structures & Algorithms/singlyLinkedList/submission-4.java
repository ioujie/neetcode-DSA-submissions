class LinkedNode {
    int val;
    LinkedNode next; 

    public LinkedNode(int val) {
        this.val = val;
        this.next = null;
    }

}

class LinkedList {

    private LinkedNode head;
    private LinkedNode tail;

    public LinkedList() {
        this.head = new LinkedNode(-1);
        this.tail = this.head;
    }

    public int get(int index) {
        LinkedNode cur = this.head.next;
        if(cur == null) {
            return -1;
        }
        for(int i = 0; i < index; ++i) {
            if(cur.next == null) {
                return -1;
            }
            cur = cur.next;
        }
        return cur.val;
    }

    public void insertHead(int val) {
        LinkedNode newHead = new LinkedNode(val);
        newHead.next = head.next;
        head.next = newHead;
        if(newHead.next == null) {
            tail = newHead;
        }
    }

    public void insertTail(int val) {
        LinkedNode newTail = new LinkedNode(val);
        this.tail.next = newTail;
        this.tail = newTail;
    }

    public boolean remove(int index) {
        if(get(index) == -1) {
            return false;
        } else {
            LinkedNode cur = this.head;
            for(int i = 0; i < index; i++) {
                cur = cur.next;
            } 
            cur.next = cur.next.next;
            if(cur.next == null) {
                this.tail = cur;
            }
        }
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> vals = new ArrayList<>();
        LinkedNode cur = this.head.next;
        if(cur == null) {
            return vals;
        }
        while(cur.next != null) {
            vals.add(cur.val);
            cur = cur.next;
        }
        vals.add(cur.val);
        return vals;
    }
}
