class Solution:
    def calculateTax(self, brackets, income) -> float:
        pointer = 0
        tax = 0.0
        money_left = income
        
        # while brackets[pointer][0] - brackets[pointer-1][0] < money_left and pointer < len(brackets):
        for pointer in range(len(brackets)):
            # initialization
            if pointer == 0:
                if money_left > brackets[pointer][0]:
                    money_left -= brackets[pointer][0]
                    print(f"money_left is {money_left}")
                    if money_left > 0:
                        tax += (brackets[pointer][0] * brackets[pointer][1]) / 100.0
                        # pointer += 1
                else:
                    money_left = brackets[pointer][0] - money_left
                    if money_left > 0:
                        tax += (brackets[pointer][0] * brackets[pointer][1]) / 100.0

            # check the gap between pointer & pointer-1
            else:
                gap = brackets[pointer][0] - brackets[pointer-1][0]
                if money_left > (gap):
                    tax += (gap * brackets[pointer][1]) / 100.0
                    money_left -= gap
                else:
                    tax += (money_left * brackets[pointer][1]) / 100.0
                    money_left -= money_left
                print(f"tax is {tax}")
                # pointer += 1


        print(tax)
            
if __name__ == '__main__':
    run = Solution()
    run.calculateTax([[1,0],[4,25],[5,50]], 2)








# ANS
# class Solution:
#     def calculateTax(self, brackets: List[List[int]], income: int) -> float:
#         x = income
#         ans = 0  
#         pre = 0
#         for u, p in brackets:
#             if x > u:
#                 ans += p * (u - pre) / 100
#                 income -= (u - pre)  
#                 pre = u
#             else: 
#                 ans += income * p / 100
#                 break
            
#         return ans