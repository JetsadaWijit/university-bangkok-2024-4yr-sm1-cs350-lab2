class Node:
    def __init__(self, id, fName, lName, score):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.score = score
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertSorted(self, id, fName, lName, score):
        newNode = Node(id, fName, lName, score)

        # If the list is empty or the new node should be at the head
        if self.head is None or self.head.id > newNode.id:
            newNode.next = self.head
            self.head = newNode
        else:
            # Find the correct position to insert the new node
            cur = self.head

            while cur.next is not None and cur.next.id < newNode.id:
                cur = cur.next

            newNode.next = cur.next
            cur.next = newNode

    def update(self, id, fName, lName, score):
        cur = self.head

        while cur:
            if cur.id == id:
                cur.score += score  # Add the new score to the existing score
                return
            cur = cur.next

        # If ID not found, insert as a new node
        self.insertSorted(id, fName, lName, score)

    def display(self):
        cur = self.head

        while cur:
            print(f"{cur.id} {cur.fName} {cur.lName} {cur.score}")
            cur = cur.next
