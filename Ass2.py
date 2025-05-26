class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node with value: {data}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added node with value: {data}")

    def print_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise ValueError("Index must be a positive integer.")
        if n == 1:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted head node with value: {deleted_value}")
            return
        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            raise IndexError("Index out of range.")
        deleted_value = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with value: {deleted_value}")

if __name__ == "__main__":
    ll = LinkedList()
    try:
        ll.delete_nth_node(1)
    except Exception as e:
        print(f"Exception: {e}")
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.print_list()
    try:
        ll.delete_nth_node(2)
    except Exception as e:
        print(f"Exception: {e}")
    ll.print_list()
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"Exception: {e}")
    ll.print_list()
