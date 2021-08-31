class Stack:
    def __init__(self):
        self.array = []

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i], end='  ')

    def peek(self): #returns the topmost elemrnt in the stack / the last element in the array.
        return self.array[len(self.array)-1]

    def push(self, value): # adds an element to the top of the stack / adds an element at the end of the array
        self.array.append(value)
        return

    def pop(self): #removes the topmost element in the stack / removes the last element in the array
        if len(self.array) == 0:
            print("Stack is empty. Nothing to pop.")
            return
        else:
            self.array.pop()
            return

if __name__ == '__main__':

    stack = Stack()
    stack.push("Good morning!")
    stack.push("Have")
    stack.push("a")
    stack.push("nice")
    stack.push("day!")
    stack.print_stack()

    # day!  nice  a  Have  Good morning!

    stack.pop()
    stack.print_stack()

    # nice  a  Have  Good morning!

    stack.peek()

    # 'nice'
