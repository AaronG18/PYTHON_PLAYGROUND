import collections

class Solution:
    def numWays(self, n: int, relation, k) -> int:
        # initialize data as src-dest dict list
        edges = collections.defaultdict(list)
        for edge in relation:
            src = edge[0] 
            dst = edge[1]
            edges[src].append(dst)
            print(f"line 10, current edge is: {src}:{edges[src]}")

        # initialize vars
        steps = 0
        queue = collections.deque([0])

        # keep going if there is still node in queue and steps < k
        while queue and steps < k:
            print(f"line 19, current queue is:{queue}")
            steps += 1
            size = len(queue)
            for i in range(size):
                index = queue.popleft()
                to = edges[index]
                print(f"current to is: {to}")
                for nextIndex in to:
                    queue.append(nextIndex)
                    print(f"queue in line 28 is: {queue}")
        ways = 0
        if steps == k:
            # if already reached depth 3 for all nodes, then we can check all the nodes if it match the value of k then way+=1
            while queue:
                print(f"line 32 queue is: {queue}")
                if queue.popleft() == n - 1:
                    ways += 1    
        print(ways) 

if __name__ == '__main__':
    run = Solution()
    run.numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
