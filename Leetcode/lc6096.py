import bisect
from sys import setprofile

class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()
        len_potions = len(potions)
        res = [0 for _ in range(len(spells))]
        print(f"len of potions is {len_potions}")
        print(f"current res is {res}")
        count = 0
        print("------------------------")

        for x in spells:
            # x * y >= success, y >= success/x, y > success//x
            target = (success) // x
            print(f"current target is {target}")
            bis_right = bisect.bisect_right(potions, target)
            print(potions)
            print(f"{len_potions-bis_right} # of elements bigger than target @ {bis_right}")
            res[count] = len_potions-bis_right
            count += 1
            print("*************************")
        print(res)


if __name__ == '__main__':
    run = Solution()
    run.successfulPairs([5,1,3],  [1,2,3,4,5], 7)

# init attempt, works but slow@220611
# class Solution:
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#         n = len(spells)
#         m = len(potions)
#         pairs = [0 for _ in range(n)]
#         print(pairs)
        
#         for i in range(n):
#             count = 0
#             for j in range(m):
#                 if spells[i] * potions[j] >= success:
#                     print(f"s * p = {spells[i]} * {potions[j]}")
#                     count+=1
#             pairs[i] = count
#         return pairs


# ori ans
    # def successfulPairs(self, spells, potions, success: int):
    #     potions.sort()
    #     len_potions = len(potions)
    #     print(f"len of potions is {len_potions}")

    #     print([len_potions - bisect.bisect_right(potions, (success - 1) // x) for x in spells])