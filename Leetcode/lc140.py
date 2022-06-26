from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict):
        # like redis, cache, same params get res from cache, fast
        @lru_cache(None)
        def backtrack(index: int):
            print(f"current index is {index}")
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                print(f"curent word is {word}")
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    print(f"cur nextWordBreaks is :{nextWordBreaks}")
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans
        
        # main run
        wordSet = set(wordDict)
        breakList = backtrack(0)


        # final part, reverser save
        print('________________________________')
        for words in breakList:
            print()
            print([" ".join(words[::-1])])
        # return [" ".join(words[::-1]) for words in breakList]

if __name__ == "__main__":
    run = Solution()
    run.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
