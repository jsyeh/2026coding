# week05-4.py 昨天的挑戰題
# LeetCode 3546. Equal Sum Grid Partition I
# grid 矩陣，能否「切一刀」兩邊和「剛好相同」
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid])  # 先把total算出來

        preSum = 0  # 利用 prefix sum 技巧「上到下」逐row相加
        for row in grid:  # grid 裡，每個 row 逐一處理
            preSum += sum(row)  # 加入 preSum 變數
            if total - preSum == preSum:  # 如果「下半==上半」
                return True  # 就成功「切一半」

        preSum = 0  # 利用 prefix sum 技巧「左到右」逐col相加
        for col in zip(*grid):  # grid 先用 zip(*星號) 對角線翻轉，取出col
            preSum += sum(col)  # grid 裡，每個 col 逐一加到 preSum 裡
            if total - preSum == preSum:  # 如果「右半==左半」
                return True  # 就成功「切一半」

        return False  # 如果「所有的切法」都沒成功，就失敗