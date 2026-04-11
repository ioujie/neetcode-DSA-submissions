class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        int n = s.length();
        if (n % 2 != 0) {
            return false;
        }
        for (int i = 0; i < n; ++i) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                stack.push(s.charAt(i));
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else if (stack.peek() == '(' && s.charAt(i) == ')') {
                    stack.pop();
                    continue;
                } else if (stack.peek() == '[' && s.charAt(i) == ']') {
                    stack.pop();
                    continue;
                } else if (stack.peek() == '{' && s.charAt(i) == '}') {
                    stack.pop();
                    continue;
                } else {
                    return false;
                }
            }
        }
        return (stack.isEmpty()) ? true : false;
    }
}
