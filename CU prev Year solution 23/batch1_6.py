class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if self.isempty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_item = self.stack.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item

    def peek(self):
        if self.isempty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            peeked_item = self.stack[-1]
            print(f"Top item of the stack is: {peeked_item}")
            return peeked_item

    def isempty(self):
        return len(self.stack) == 0

stack = Stack()
# Push some items onto the stack
stack.push(5)
stack.push(10)
stack.push(15)
# Peek at the top item of the stack
stack.peek()
# Pop items from the stack
stack.pop()
stack.pop()
stack.pop()
stack.pop()  # Attempting to pop from empty stack


