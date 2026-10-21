class MinStack {
public:
    vector<int> stack;
    vector<int> minStack;
    MinStack() {
    }
    
    void push(int val) {
        if (minStack.empty()) minStack.push_back(val);
        else if (minStack.back() >= val) minStack.push_back(val);

        stack.push_back(val);
    }
    
    void pop() {
        if(stack.back() == minStack.back()) minStack.pop_back();
        stack.pop_back();

    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return minStack.back();
    }
};
