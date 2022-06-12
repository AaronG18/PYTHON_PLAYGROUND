class Solution:
    def partition(self, s):
        n = len(s)
        print(f"n is {n}")
        f = [[True] * n for _ in range(n)]
        print(f"f is {f}")

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        print("**********************")
        print(f"f is {f}")

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            print(f"ans is {ans} ret is {ret}")
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()
                print(f"in dfs for, ans is {ans} ret is {ret}")

        dfs(0)
        return ret

if __name__ == '__main__':
    run = Solution()
    run.partition("aab")