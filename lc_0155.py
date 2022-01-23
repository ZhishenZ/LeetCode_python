from cmath import inf


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [ inf ] #
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        val =self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
print(minStack.push(0));
print(minStack.push(1));
print(minStack.push(0));
print(minStack.getMin()); #// return -3
print(minStack.pop());
print(minStack.getMin()); #// return 0
print("########################")
minStack2 = MinStack();
print(minStack2.push(-2));
print(minStack2.push(0));
print(minStack2.push(-3));
print(minStack2.getMin()); #// return -3
print(minStack2.pop());
print(minStack2.top());    #// return 0
print(minStack2.getMin()); #// return -2