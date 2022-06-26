# class Solution {
#   public int minimumNumbers(int num, int k) {
#     if (num == 0) return 0;
#     if (k == 0) return num % 10 == 0 ? 1 : -1;

#     for (int i = 1; i <= num / k + 1; i++) {
#       int res = num - i * k;
#       if (res % 10 == 0) return i;
#     }
#     return -1;
#   }
# }

class Solution:
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1

        print(f"upper limit for loop is:{num//k+1}")
        for i in range(1, num//k+1):
            res = num - i * k
            print(f"i*k is {i*k}")
            print(f"res is {res}")
            if res % 10 == 0:
                return i
        return -1

if __name__ == '__main__':
    run = Solution()
    print(run.minimumNumbers(58, 9))
        
