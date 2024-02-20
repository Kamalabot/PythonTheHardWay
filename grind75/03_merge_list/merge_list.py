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
    ptr1 = ListNode(val=list1[0])
    ptr2 = ListNode(val=list2[0])
    curr1 = ptr1
    curr2 = ptr2
    for x in list1[1:]:
        curr1.next = ListNode(x)
        curr1 = curr1.next
    for x in list2[1:]:
        curr2.next = ListNode(x)
        curr2 = curr2.next
    # print(get_elem(link1))
    # print(get_elem(link2))
    # Create a dummy node as the head of the merged linked list.
    dumy = ListNode()
    # Initialize two pointers, one for each of the input lists: ptr1 for list1 and ptr2 for list2. Set both pointers to the heads of their respective lists.
    # Create a pointer, called curr, and initially point it to the dummy node.
    curr = dumy
    # Repeat steps 4-5 until either ptr1 or ptr2 becomes null (reached the end of the respective list).
    while ptr1 and ptr2:
        # Compare the values of ptr1 and ptr2. 
        if ptr1.val <= ptr2.val:
            # a. If the value of ptr1 is smaller than or equal to ptr2, set the next node of curr to ptr1. 
            curr.next = ptr1
            # Move ptr1 to the next node in list1. 
            ptr1 = ptr1.next
        else:
            # b. Otherwise, set the next node of curr to ptr2. 
            curr.next = ptr2
            # Move ptr2 to the next node in list2.
            ptr2 = ptr2.next
        # Move curr to the next node.
        curr = curr.next
    # Once one of the pointers becomes null,
    curr.next = ptr1 if ptr1 else ptr2 
    # Return the next node of the dummy node as the 
    # head of the merged linked list.
    x = get_elem(dumy.next)

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
# assert merger_simp(list1, list2) == Output  # Output
assert mergeTwoLists(list1, list2) == Output  # Output

# list1 = []
# list2 = []
# Output = []
# assert mergeTwoLists(list1, list2) == None  # Output

# list1 = []
# list2 = [0]
# Output = [0]
# assert mergeTwoLists(list1, list2) == None  # Output