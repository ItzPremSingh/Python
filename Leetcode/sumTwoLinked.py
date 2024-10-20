class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.next = None
        self.val = val


def format(node: ListNode) -> None:
    while node.next is not None:
        print(node.val)
        node = node.next


class Solution:
    def addTwoNumbers(self, firstNode: ListNode, secondNode: ListNode) -> ListNode:
        return ListNode()


listNode = ListNode(0)
current = listNode

for number in range(1, 11):
    newNode = ListNode(number)
    current.next = newNode
    current = newNode


format(listNode)
