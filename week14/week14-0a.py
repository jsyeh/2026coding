from heapq import *
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # code here
        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return nums[0]








        

# Do not modify the lines below
nums = list(map(int, input()[1:-1].split(',') ))
k = int(input())
print(Solution().findKthLargest(nums, k))