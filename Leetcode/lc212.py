from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        print(f"word in insert is {word}")
        cur = self
        for c in word:
            cur = cur.children[c]
            print(f"cur is {cur}")
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        print(f"inital trie is: {trie.children}+{trie.word}")
        for word in words:
            trie.insert(word)
        print(f"2nd trie is: {trie.children}+{trie.word}")

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        print(list(ans))


if __name__ == '__main__':
    run = Solution()
    run.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])

# could get this at all in 20220619, run thru the concep of trie & dfs but still dont get this

