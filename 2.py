class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

def createList(values):
    head=Node(values[0])
    cur=head
    for val in values[1:]:
        cur.next=Node(val)
        cur=cur.next
    return head

def printlist(head):
    cur=head
    while cur:
        print(cur.data,end=" -> ")
        cur=cur.next
    print("None")

             

