class MinStack {

    private Deque<Integer> stack;
    private Deque<Integer> minstack;

    public MinStack() {
        this.stack = new ArrayDeque<>();
        this.minstack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minstack.isEmpty() || minstack.peek() >= val) {
            minstack.push(val);
        }
    }
    
    public void pop() {
        if (stack.peek().equals(minstack.peek())) {
            minstack.pop();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minstack.peek();
    }
}
