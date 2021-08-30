from linked_list_implementation import Node, LinkedList

linked_list = LinkedList()

for i in range(5, 11):
    linked_list.append(i)

linked_list.print_list()

# 5-->6-->7-->8-->9-->10-->None

def reverse(linked_list):
    if linked_list.length == 0:
        print("The list is empty. Nothing to reverse")

    elif linked_list.length == 1:
        return linked_list

    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second != None:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list


reversed_list = reverse(linked_list)
reversed_list.print_list()

# 10-->9-->8-->7-->6-->5-->None
