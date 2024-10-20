from linklist import ListNode, push, display


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2

        sumList = ListNode(current1.val + current2.val)
        current3 = sumList

        current1 = current1.next
        current2 = current2.next

        carry = 0

        while current2:
            num1, num2 = current1.val, current2.val

            _sum = num1 + num2

            if _sum > 9:
                carry = 1
                _sum -= 10

            elif carry:
                _sum += 1
                carry = 0

            newNode = ListNode(_sum)

            current3.next = newNode
            current3 = newNode

            current1, current2 = current1.next, current2.next

        while current1:
            num1 = current1.val
            if carry:
                num1 += 1
                carry = 0

            if num1 > 9:
                carry = 1
                num1 -= 10

            newNode = ListNode(num1)
            current3.next = newNode
            current3 = newNode

            current1 = current1.next

        return sumList


num1 = ListNode()
num2 = ListNode()

push(num1, [2, 4, 3])
push(num2, [5, 6])


sum = Solution().addTwoNumbers(num1, num2)
display(sum)
