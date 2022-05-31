import unittest

# Singly linked list implementation

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        n = self.head
        res = []

        while n:
            res.append(str(n.data))
            n = n.next
        
        return "->".join(res[::-1])

    def insertBefore(self, data, new_data):
        if self.head is None:
            return

        if self.head.data == data:
            node = Node(new_data)
            node.next = self.head
            self.head = node
            return

        cur = self.head
        while cur.next:
            if cur.next.data == data:
                node = Node(new_data)
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next

    # insert at the end
    def insert(self, data):
        node = Node(data)

        # empty list, insert node as head
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
            else:
                cur = cur.next

class TestSort(unittest.TestCase):
    def test_linked_list(self):
        # create linked list:
        # 1 -> 5 -> 4 -> 3 
        # delete(4) -> 1 -> 5 -> 3
        # delete(1) -> 5 -> 3
        ll = LinkedList()
        ll.head = Node(1)
        ll.insert(5)
        ll.insert(4)
        ll.insert(3)
        ll.insertBefore(4, 2)
        ll.insert(2)
        print(ll)

        self.assertEqual(str(ll), "1->5->4->2->3")
        ll.delete(2)
        ll.delete(4)
        self.assertEqual(str(ll), "1->5->3")

        ll.delete(1)
        self.assertEqual(str(ll), "5->3")

if __name__ == "__main__":
    print("singly linked list")
    unittest.main()