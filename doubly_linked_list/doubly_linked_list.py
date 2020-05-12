"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

"""
Julie's Notes:
https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png
https://www.thecodingdelight.com/doubly-linked-list/·

Why is a good idea use DLL?
- A DLL allows us to go in both directions forward and backward
- The delete operation in DLL is more efficient if pointer to the node to be
    deleted is given.
- We can quickly insert a new node before a given node
In singly linked list, to delete a node, pointer to the previous node is needed.
To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.

Disadvantage:
- It uses extra memory when compared to array and singly linked list.
- Since elements in memory are stored randomly, hence elements are accessed sequentially no direct access is allowed.

1) Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though.
2) All operations require an extra pointer previous to be maintained.
For example, in insertion, we need to modify previous pointers together with next pointers. 
 

Insertion
A node can be added in four ways
1) At the front of the DLL
2) After a given node.
3) At the end of the DLL
4) Before a given node.
"""



class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        # the order is self, new node, current_next
        # we're gonna to change the next of the self point to the new node,
        # so we have to record the current_next, in order to point the current_next prev
        # back to the new node.
        current_next = self.next 
        # set the self node next points to the node we need to add after.
        # creat the new node, and give it the prev = self, next = current_next
        self.next = ListNode(value, self, current_next)
        
        if current_next: # if there have one node after the newnode.
            current_next.prev = self.next # set the prev point to the new node"self.next"

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        # set the self node prev points to the node we need to add before.
        # creat the new node, and give it the prev = current_prev, next = self.
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # If LL is empty
        if not self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return
        # If node is head
        # If node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        
        # If node is in middle
        else:
            node.delete()

        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # Max max var
        # Loop through nodes via node.next
        # If node.value is higher, update max
        # return max
        if self.head == None:
            return None
        max_node = self.head.value
        actual_node = self.head
        while actual_node:
            if actual_node.value > max_node:
                max_node = actual_node.value
            actual_node = actual_node.next
        return max_node
