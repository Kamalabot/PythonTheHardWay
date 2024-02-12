problemStatement = """You are given the heads of two sorted linked lists list1
and list2.Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
link = "https://leetcode.com/problems/merge-two-sorted-lists/description/"
solution = "reviewing linked list"

# Using the ListNode class
class ListNode(object):
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    # implement append method
    def append(self, val):
        # check if head is none
        if self.head is None:
            self.head = ListNode(val)
            self.length += 1
        # if not none, the assign it to a observer
        curr = self.head
        # enter endless loop
        while True:
            # check if at tail node
            if curr.next is None:
                # append the next node
                curr.next = ListNode(val)
                self.length += 1
                # exit loop
                break
            # move to the next element
            curr = curr.next

    def traverse(self):
        # create a store for elements
        store = []

        if self.head is None:
            return store
        # assign head to observer
        curr = self.head
        store.append(curr.val)
        # enter endless loop
        while True:
            # check if curr is tail
            if curr.next is None:
                break
            # move to the next element
            curr = curr.next
            store.append(curr.val)
        # return the store list
        return store

    def __len__(self):
        return self.length


def mergeTwoLists(list1, list2):
    # create two linked lists
    ll1 = LinkedList()
    ll2 = LinkedList()
    # if list has elements then append to ll1
    if len(list1) > 0:
        for val in list1:
            ll1.append(val)

    # repeat above
    if len(list2) > 0:
        for val in list2:
            ll2.append(val)
 
    print(len(ll1))
    print(len(ll2))
    print(ll1.traverse())
    print(ll2.traverse())


list1 = [1, 2, 4]
list2 = [1, 3, 4]
Output = [1, 1, 2, 3, 4, 4]
assert mergeTwoLists(list1, list2) == None  # Output

# list1 = []
# list2 = []
# Output = []
# assert mergeTwoLists(list1, list2) == None  # Output

# list1 = []
# list2 = [0]
# Output = [0]
# assert mergeTwoLists(list1, list2) == None  # Output