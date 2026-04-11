class MinStack {

    private List<Integer> stack;

    public MinStack() {
        this.stack = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
    }
    
    public void pop() {
        stack.get(stack.size() - 1);
        stack.remove(stack.size() - 1);
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        int min = stack.get(0);
        for (int i = 0; i < stack.size(); ++i) {
            if (stack.get(i) < min) {
                min = stack.get(i);
            }
        }
        return min;
    }
}
