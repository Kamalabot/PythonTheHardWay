problemStatement = """You are given the heads of two sorted linked lists list1
and list2.Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
link = "https://leetcode.com/problems/merge-two-sorted-lists/description/"
solution = "reviewing linked list"

approach = """
Take a head of a l1, assign its next node to a temp variable
Take the head of the l2, and make it next of the l1's head. 
"""

# Using the ListNode class
class ListNode(object):
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class singleLinked(object):
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = ListNode(val)


def get_elem(head):
    elements = []
    if head is None:
        return elements
    curr = head
    while curr.next is not None:
        # print(curr.val)
        elements.append(curr.val)
        curr = curr.next
    elements.append(curr.val)
    return elements


def mergeTwoLists(list1, list2):
    # 1st element is head
    link1 = ListNode(val=list1[0])
    link2 = ListNode(val=list2[0])
    curr1 = link1
    curr2 = link2
    for x in list1[1:]:
        curr1.next = ListNode(x)
        curr1 = curr1.next
    for x in list2[1:]:
        curr2.next = ListNode(x)
        curr2 = curr2.next
    # print(get_elem(link1))
    # print(get_elem(link2))
    # start a while loop to traverse list1
    while link1.next is not None:
        # assign l1-head's next element to temp1
        temp1 = link1.next
        # assign the l2-head as l1_head.next 
        link1.next = link2
        # start traversing list2
        while link2.next is not None:
            # assign the next of list2 to temp 2
            temp2 = link2.next
            # assign temp1 from above as list2.next
            link2.next = temp1
            # assign temp2 to list2  
            link2 = temp2.next
        # assign next of temp1 to list1
        link1 = temp1.next
    x = get_elem(link1)
    print(x)
    return x


# below cannot be a solution
def merger_simp(list1, list2):
    newl = [] 
    for ind, x in enumerate(list1):
        newl.append(x)
        newl.append(list2[ind])
    return newl


list1 = [1, 2, 4]
list2 = [1, 3, 4]
Output = [1, 1, 2, 3, 4, 4]
# assert mergeTwoLists(list1, list2) == Output  # Output
assert merger_simp(list1, list2) == Output  # Output

# list1 = []
# list2 = []
# Output = []
# assert mergeTwoLists(list1, list2) == None  # Output

# list1 = []
# list2 = [0]
# Output = [0]
# assert mergeTwoLists(list1, list2) == None  # Output