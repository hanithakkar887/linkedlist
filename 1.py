class Node:
    def __init__(self,item):
        self.data=item
        self.next=None
def createList(values):
    if not values:
        return None
    head=Node(values[0])
    cur=head
    for val in values[1:]:
        cur.next=Node(val)
        cur=cur.next
    return head

values=[1,3]

def printList(head):
    cur=head
    while cur:
        print(cur.data,end="->")
        cur=cur.next
    print("None")


def fillGaps(head):
    if not head or not head.next:
        return head
    cur=head
    # dif=None
    while cur and cur.next:
        next_node=cur.next
        dif=next_node.data-cur.data

        while dif>1:
            new_node=Node(cur.data+1)
            new_node.next=cur.next
            cur.next=new_node

            cur=new_node
            dif=next_node.data-cur.data
        cur=next_node
    return head    




head=createList(values)
print("_________________befor________________");
printList(head)

head=fillGaps(head)
print("_________________after________________");
printList(head)
# print(createList(values))
    


























# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.next = None

# def fillGaps(head):
#     cur = head
#     while cur and cur.next:
#         next_node = cur.next
#         dif = next_node.data - cur.data
        
#         while dif > 1:
#             new_node = Node(cur.data + 1)
#             new_node.next = cur.next
#             cur.next = new_node
            
#             cur = new_node
#             dif = next_node.data - cur.data
#         cur = next_node
#     return head

# # Helper function to print the linked list
# def printList(head):
#     cur = head
#     while cur:
#         print(cur.data, end=" -> ")
#         cur = cur.next
#     print("None")

# # Helper function to create a linked list from a list of values
# def createLinkedList(values):
#     if not values:
#         return None
#     head = Node(values[0])
#     cur = head
#     for value in values[1:]:
#         cur.next = Node(value)
#         cur = cur.next
#     return head

# # Example usage:
# values = [1, 3, 6]
# head = createLinkedList(values)
# print("Original list:")
# printList(head)

# head = fillGaps(head)
# print("List after filling gaps:")
# printList(head)
