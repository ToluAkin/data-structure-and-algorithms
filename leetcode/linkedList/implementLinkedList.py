class MyLinkedList:
    def __init__(self):
        myList = [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

        self.data = myList
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        return self.data[index][0]

    def addAtHead(self, val: int) -> None:
        head = self.data[0]
        self.val = [val]

        if not head:
            head.append(val) 
            self.data = [head] + self.data[1:]
        else:
            self.data = [self.val] + self.data
        return self.data

    def addAtTail(self, val: int) -> None:
        self.val = val
        if not self.data:
            self.data.append(self.val)
        else:
            new_node = [self.val]
            self.data = self.data + [new_node]
        return self.data

    def addAtIndex(self, index: int, val: int) -> None:
        self.val = val
        new_node = [self.val]
        len_node = len(self.data)

        if index == 0:
            self.addAtHead(new_node)
            return
        elif index == len_node:
            self.addAtTail(new_node)
        elif index > len_node:
            return
        else:
            front = self.data[:index]
            back = self.data[index + 1:]
            self.data = front + [new_node] + back
        return self.data

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            head = self.data[0]
            if head:
                self.data = self.data[1:]
        elif index < len(self.data):
            current = self.data[index]
            if len(current) == 1:
                self.data.pop(index)
            else:
                self.data[index] = current[1:]
        return self.data

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
    print(myLinkedList.addAtHead(2)) # 2->7->7
    print(myLinkedList.addAtHead(1)) # 1->2->7->7
    print(myLinkedList.addAtIndex(3, 0)) # 1->2->0->7
    print(myLinkedList.deleteAtIndex(2)) # 1->2->7->1
    print(myLinkedList.addAtHead(6)) # 6->1->2->7
    print(myLinkedList.addAtTail(4)) 
    print(myLinkedList.get(4)) # 1
    print(myLinkedList.addAtHead(4)) # 4->6->1->2->7
    print(myLinkedList.addAtIndex(5, 0)) # 4->6->1->2->0
    print(myLinkedList.addAtHead(6)) # 6->4->6->1->2->0