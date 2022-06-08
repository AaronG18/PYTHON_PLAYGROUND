'''
方法三：数学法
说明

方法三涉及逆向思维，是一种没见过就不太可能想出来，读过题解也很容易忘记的方法。

思路

反过来想这个问题：如果我们可以做 tt 次操作，而且有 kk 个鸡蛋，那么我们能找到答案的最高的 nn 是多少？我们设 f(t, k)f(t,k) 为在上述条件下的 nn。如果我们求出了所有的 f(t, k)f(t,k)，那么只需要找出最小的满足 f(t, k) \geq nf(t,k)≥n 的 tt。

那么我们如何求出 f(t, k)f(t,k) 呢？我们还是使用动态规划。因为我们需要找出最高的 nn，因此我们不必思考到底在哪里扔这个鸡蛋，我们只需要扔出一个鸡蛋，看看到底发生了什么：

如果鸡蛋没有碎，那么对应的是 f(t - 1, k)f(t−1,k)，也就是说在这一层的上方可以有 f(t - 1, k)f(t−1,k) 层；

如果鸡蛋碎了，那么对应的是 f(t - 1, k - 1)f(t−1,k−1)，也就是说在这一层的下方可以有 f(t - 1， k - 1)f(t−1，k−1) 层。

因此我们就可以写出状态转移方程：

f(t, k) = 1 + f(t-1, k-1) + f(t-1, k)
f(t,k)=1+f(t−1,k−1)+f(t−1,k)

边界条件为：当 t \geq 1t≥1 的时候 f(t, 1) = tf(t,1)=t，当 k \geq 1k≥1 时，f(1, k) = 1f(1,k)=1。

那么问题来了：tt 最大可以达到多少？由于我们在进行动态规划时，tt 在题目中并没有给出，那么我们需要进行到动态规划的哪一步呢？可以发现，操作次数是一定不会超过楼层数的，因此 t \leq nt≤n，我们只要算出在 f(n, k)f(n,k) 内的所有 ff 值即可。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if n == 1:
            return 1
        print(f"f is {n+1} rows(floor+1) and {k+1} columns(eggs+1)")

        '''
        assume f(t, k) = n, we can do t moves with k eggs
        '''
        f = [[0] * (k + 1) for _ in range(n + 1)]
        print(f)
        print("--------------------------")
        for i in range(1, k + 1):
            print("one moves, no matter # eggs you have, = 1")
            f[1][i] = 1
            print(f)
        print("--------------------------")

        # initialize ans
        ans = -1

        # f(t,k) <= n, max moves is n, min moves is 1, and 1 is already initialized, so starts from 2
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                # total floor = current floor + f[i-1][j-1] beneth and f[i-1][j] above
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
                print(f"current i is {i} and current j is {j}")
                print(f"current f[i][j] is {f[i][j]}")
                print(f"{f[i - 1][j - 1]} beneth and {f[i - 1][j]} above")

                print("******************")
                print(f"n=f[i][k] is {f[i][k]}")

            # f(t, k) <= n, when bigger than n, time to quit, you cant move higher than n floors
            if f[i][k] >= n:
                ans = i
                break
        print("--------------------------")
        print(ans)

if __name__ == '__main__':
    run = Solution()
    run.superEggDrop(2, 6)