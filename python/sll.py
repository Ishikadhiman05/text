class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printll(head):
        cur=head
        while cur!=None:
            print(cur.data,end="->")
            cur=cur.next
        print("None")
def insert_at_start(head, data):
    temp=Node(data)
    temp.next=head
    head=temp
    return head

def insert_at_last(head, data):
     temp=Node(data)
     cur=head
     while cur.next!=None:
          cur=cur.next
     cur.next=temp
     return head

def reverse_linked_list(head):
    '''arr = []
    cur = head
    while cur is not None:
        arr.append(cur.data)
        cur=cur.next
    arr.reverse()
    print(arr)
    '''
    prev=None
    cur=head
    while cur is not None:
        next_node=cur.next
        cur.next=prev
        prev=cur
        cur=next_node
    return prev


node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
head=node1
head=insert_at_start(head, 40)
head=insert_at_last(head, 50)
printll(head)
arrr=reverse_linked_list(head)
print(arrr)
