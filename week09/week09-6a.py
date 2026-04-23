# week09-6.py 學習計畫 Linked list 第2題
# LeetCode 328. Odd Even Linked List 偶數堆、奇數堆,串起來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 下面是在 Linked List 的世界進行處理, 比較有難度
        if head==None or head.next==None: return head  # 沒辦法
        ans = ans1 = head  # 「第奇數個」放在前面
        ans20 = ans2 = head.next # 「第偶數個」放在後面
        head = head.next.next
        while head != None:
            ans1.next, head = head, head.next
            ans1 = ans1.next
            if head != None:
                ans2.next, head = head, head.next
                ans2 = ans2.next
        ans1.next = ans20
        ans2.next = None
        return ans