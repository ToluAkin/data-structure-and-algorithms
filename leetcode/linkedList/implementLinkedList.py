class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        new_node = self.head
        while new_node is not None:
            yield new_node.val
            new_node = new_node.next

    
    def __len__(self):
        count = 0
        new_node = self.head
        while new_node is not None:
            count += 1
            new_node = new_node.next
        return count

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self):
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            new_node = self.head
            while new_node.next is not None:
                new_node = new_node.next
            new_node.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        len_node = len(self)
        new_node = self.head

        if index < 0 or index > len_node:
            return None
        if index == 0:
            self.addAtHead(new_node)
            return
        if index == len_node:
            self.addAtTail(new_node)
            return
        count = 0
        while new_node:
            if count == index - 1:
                node = Node(val)
                node.next = new_node.next
                new_node.next = node
                break
            new_node = new_node.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > len(self) - 1:
            return -1
        if index == 0:
            self.head = self.head.next
        
        count = 0
        new_node = self.head
        while new_node:
            if count == index - 1:
                new_node.next = new_node.next.next
                break
            new_node = new_node.next
            count += 1

# Example usage
if __name__ == "__main__":
    # myList = [[], [1], [3], [1, 2], [1], [1], [1]]
    # myLinkedList = MyLinkedList()
    # print(f"{myLinkedList.addAtHead(1)}")
    # print(myLinkedList.addAtTail(3))
    # print(myLinkedList.addAtIndex(1, 2))    # linked list becomes 1->2->3
    # print(myLinkedList.get(1))             # return 2
    # print(myLinkedList.deleteAtIndex(1))  # now the linked list is 1->3
    # print(myLinkedList.get(1))
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    
    myList = [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    myLinkedList = MyLinkedList()
    print(myLinkedList.addAtHead(7)) # 7->7
    # print(myLinkedList.addAtHead(2)) # 2->7->7
    # print(myLinkedList.addAtHead(1)) # 1->2->7->7
    # print(myLinkedList.addAtIndex(3, 0)) # 1->2->0->7
    # print(myLinkedList.deleteAtIndex(2)) # 1->2->7->1
    # print(myLinkedList.addAtHead(6)) # 6->1->2->7
    # print(myLinkedList.addAtTail(4)) 
    # print(myLinkedList.get(4)) # 1
    # print(myLinkedList.addAtHead(4)) # 4->6->1->2->7
    # print(myLinkedList.addAtIndex(5, 0)) # 4->6->1->2->0
    # print(myLinkedList.addAtHead(6)) # 6->4->6->1->2->0