class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


head = ListNode(0)
current = head


for val in [
    7,
    7,
    7,
    7,
    7,
]:
    new_node = ListNode(val)
    current.next = new_node
    current = new_node
