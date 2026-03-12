# week03-3.py 學習計畫 Sliding Window 第2題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# 母音 Vowels: a,e,i,o,u。長度k的小字串,最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')  # 把5個字母,變成set()
        count = 0  # 記錄目前有幾個母音
        for i in range(k):  # 找前面 k 個字母, 逐一檢查,看是不是母音
            if s[i] in vowels: count += 1  # 找到1個母音,開心!!!


        ans = total  # 離開迴圈時, 確認前k個字母, 有 count 個母音, 先當答
        N = len(s)  # 全部字串的長度 N
        for i in range(k, N):  # 右邊的每一個字母, 逐一檢查
            if s[i] in vowels: total += 1  # 右邊的頭 s[i] 又吃到1個母
            if s[i-k] in vowels: total -= 1  # 左邊尾巴 s[i-1] 吐掉,失
            ans = max(ans, total)  # 更新答案, 找最大值
        return ans