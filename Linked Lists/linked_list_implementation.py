class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head == None:
            print("The list is empty.")
            return

        else:
            current_node = self.head
            while current_node != None:
                print(current_node.value, end = '-->')
                current_node = current_node.next
            print('None')

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)

        elif index >= self.length:
            if index > self.length:
                print("Index greater than length of the list. Inserting at the end.")
                self.append(value)
            else:
                self.append(value)

        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1


    def delete(self, index):
        if self.head == None:
            print("List is empty. Nothing to delete.")

        elif index < 0:
            print("Enter a valid index.")

        elif index == 0:
            self.head = self.head.next
            if self.head.next == None:
                self.tail == self.head
            self.length -= 1
            return

        elif index >= self.length:
            index = self.length-1
            print("Index greater than length. Deleting last node.")
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.tail = current_node
            self.length -= 1

        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.length -= 1

if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(5)
    l1.append(100)
    l1.append(3)

    l1.insert(1, 25)
    l1.print_list()
    # 5-->25-->100-->3-->None

    l1.insert(2, 95)
    l1.print_list()

    # 5-->25-->95-->100-->3-->None

    l1.insert(0, 1)
    l1.print_list()

    #1-->5-->25-->95-->100-->3-->None

    l1.delete(3)
    l1.print_list()

    #1-->5-->25-->100-->3-->None

    print(l1.length)
    # 5
