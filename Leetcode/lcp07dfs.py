import collections


class Solution:
    def __init__(self, n, relation, k):
        self.ways, self.n, self.relation, self.k = 0, n, relation, k
        self.edges = collections.defaultdict(list)

    def numWays(self,) -> int:
        # initialize edge as dict
        for src, dst in self.relation:
            self.edges[src].append(dst)
            print(f"line 13 edge is: {self.edges}")

        # start from index 0, steps 0
        self.dfs(0,0)
        print(self.ways) 

    def dfs(self, index, steps):
        print(f"line 21 index is: {index} and steps is {steps}")
        print(f"line 22, current edge is {index} : {self.edges[index]}")
        if steps == self.k:
            # if depth is k
            if index == self.n-1:
                # and if index == target node
                # add 1 to ways and stop this call
                self.ways += 1
            return
        for to in self.edges[index]:
            self.dfs(to, steps+1)

if __name__ == '__main__':
    run = Solution(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
    run.numWays()