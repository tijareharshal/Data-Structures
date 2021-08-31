class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0


    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
            self.bottom = self.top

        else:
            new_node.next = self.top
            self.top = new_node
            self.length
        self.length += 1

    def pop(self):
        if self.top == None:
            print("Stack is empty. Nothing to pop.")
        else:
            self.top = self.top.next
            if self.top.next == 0:
                self.bottom = self.top
            self.length -= 1

    def print_stack(self):
        if self.top == None:
            print("Stack is empty")
        else:
            current = self.top
            while current:
                print(current.value)
                current = current.next

    def peek(self):
        if self.top == None:
            print("Stack is empty.")
        else:
            return self.top.value

if __name__ == '__main__':

    stack = Stack()
    stack.push("Good morning!")
    stack.push("Have")
    stack.push("a")
    stack.push("nice")
    stack.push("day!")
    stack.print_stack()

    # day!
    # nice
    # a
    # Have
    # Good morning!

    print(stack.length)

    # 5

    stack.pop()
    stack.print_stack()

    # nice
    # a
    # Have
    # Good morning!

    stack.pop()
    stack.print_stack()

    # a
    # Have
    # Good morning!

    print(stack.peek())

    # a

    print(stack.length)

     # 3
