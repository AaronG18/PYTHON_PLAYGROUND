class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)
        summ = 0                            # 当前子序列的值
        removed = 0                         # 记录要移除的1的个数
        for i, ch in enumerate(s[::-1]):    # 贪心：从低位到高位遍历s
            if ch == '1':                   # 判断当前位的1能否被保留
                if summ + (1<<i) > k:       # 当前位的1无法保留
                    removed += 1
                else:                       # 当前位的1可以保留
                    summ += (1<<i)
        return n - removed

if __name__ == '__main__':
    run = Solution()
    print(run.longestSubsequence("1001010", 5))