class MinStack {
    private List<Integer> stack;
    public MinStack() {
        stack = new ArrayList<Integer>();
        System.out.println(stack.toString());
    }
    
    public void push(int val) {
        stack.add(val);
        System.out.println(stack.toString());
    }
    
    public void pop() {
    stack.remove(stack.size() - 1);
    System.out.println(stack.toString());
    }
    
    public int top() {
        System.out.println(stack.toString());
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        List<Integer> sortedStack = new ArrayList<Integer>(stack);
        Collections.sort(sortedStack);
        return sortedStack.get(0);
    }
}
