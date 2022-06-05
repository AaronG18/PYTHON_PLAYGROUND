class Solution:
    def numWays(self, n, relation, k):
        # init 2d array of k+1 rows and n+1 columns
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        print(dp)
        # pass to node 0 in 0 step is 1 (to itself)
        dp[0][0] = 1
        print(dp)


        for i in range(k):
            print(f"current i is {i} and cur k is {k} and relation is {relation}")
            for edge in relation:
                print(f"current edge is {edge} and cur dp is {dp}")
                src = edge[0]
                dst = edge[1]
                dp[i + 1][dst] += dp[i][src]
                print(f"current src is {src} and cur dst is {dst}")
                print(f"cur dp[i + 1][dst] is {dp[i + 1][dst]}, # of plans to {dst} in {i+1} rows")
                print("*****************************************************************************")
            print("--------------------------------------------------------------------------------")
        print(f"final dp is {dp}")
        print(dp[k][n - 1])

if __name__ == '__main__':
    run = Solution()
    run.numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)