class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


def push(head: ListNode, data: list[int]) -> None:
    head.val = data[0]
    current = head
    for element in data[1:]:
        newNode = ListNode(element)
        current.next = newNode
        current = newNode


def display(head: ListNode) -> None:
    current = head
    while current:
        print(current.val)
        current = current.next
