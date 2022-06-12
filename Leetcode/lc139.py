class Solution:
    def wordBreak(self, s, wordDict):       
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                print(f"current i is {i} and j is {j} and s[i:j] is {s[i:j]}")
                # s[i:j] takes index i to index j-1
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
                    print(f"cur j is {j}")
                    print(f"matched ! {s[i:j]}")
                    print(dp)
        print(f"final ans is : {dp[-1]}")

    # experiment
    def wordBreakWithoutZeroFront(self, s, wordDict):       
        n=len(s)
        dp=[False]*(n)

        for i in range(n):
            for j in range(i+1,n+1):
                print(f"current i is {i} and j is {j}")
                # this would not work because there is no true dp[i], so we need to initalize one, 
                # anchor dp[0] = True can help us initialize some first words in the dict easily by 
                # getting words in the range of 0~1, 0~2,...,[0:n] in s to match dict
                # and when we see new word that match dict but we need to check if before i in all in the dict, if not, even if 
                # it meets dict but the fore part does not all in dict, so there is no point 
                # => not all words of this string in dict
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j-1]=True
                    print(f"cur s[i:j] is {s[i:j]}")
                    print(f"cur dp is {dp}")
                else:
                    print("!!!!!!!!!!d[i] false or s[i:j] not in dict!!!!!!")
                    print(s[i:j])
                    print("!!!!!!!!!!!!!!!!!!!!!!")
        print(f"final ans is : {dp} + {dp[-1]}")
        return dp[-1]


if __name__ == '__main__':
    run = Solution()

    # the last dog didnt match because at i = 6 j = 9 , s[6:9] => 6th to 8th in s, => dp[6] is false, so from index 0~6 in s
    # are not in dictionary, which is catsan
    # run.wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    run.wordBreakWithoutZeroFront("leetcode", ["leet","code"])

