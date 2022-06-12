'''
data={"全球":[{"中国":["北京","杭州","上海"]},{"美国":["华盛顿","洛杉矶","纽约"]},{"英国":["伦敦","爱丁堡","伯明翰"]}]}
#有如下一组数据类型
example=[
    {"北京":1,"杭州":0,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":0,"爱丁堡":1,"伯明翰":1},
    {"北京":1,"杭州":1,"上海":0,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":1,"爱丁堡":0,"伯明翰":1},
    {"北京":0,"杭州":0,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":0,"爱丁堡":1,"伯明翰":0},
    {"北京":0,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":0,"爱丁堡":1,"伯明翰":1},
    {"北京":1,"杭州":0,"上海":0,"华盛顿":1,"洛杉矶":1,"纽约":0,"伦敦":1,"爱丁堡":0,"伯明翰":1},
    {"北京":1,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":1,"纽约":1,"伦敦":0,"爱丁堡":1,"伯明翰":0},
    {"北京":0,"杭州":1,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":1,"爱丁堡":0,"伯明翰":1},
    {"北京":1,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":1,"爱丁堡":1,"伯明翰":0}
]
#已知data中全球对应1级,中国美国英国对应2级,"北京","杭州","上海","华盛顿","洛杉矶","纽约","伦敦","爱丁堡","伯明翰"对应3级
#1,当北京,杭州,上海其中有俩个或以上为1的时候3级加一,当华盛顿,洛杉矶,纽约其中有俩个或以上为1时候3级加一,当伦敦,爱丁堡,伯明翰其中有俩个或以上为1的时候3级加一

#2,当北京,杭州,上海连续两次或者两次以上其中有两个为1的时候中国也为1(2级加一),当华盛顿,洛杉矶,纽约连续两次或者两次以上其中有两个为1的时候美国也为1(2级加一),当伦敦,爱丁堡,伯明翰连续两次或者两次以上其中有两个为1的时候英国也为1(2级加一)

#3,当中国,美国,英国连续两次或者两次以上其中有两个为1的时候全球为1(1级加一)

#注,连续出现2次以上持续加一,例如连续两次加1,连续第三次则再加1
#通过1,2,3,用代码求出example中1级,2级,3级1的次数。
'''

class Solution():
    def __init__(self):
        # 全球一级, 国家二级, 城市三级
        self.data = {"全球": [{"中国":["北京","杭州","上海"]}, {"美国":["华盛顿","洛杉矶","纽约"]}, {"英国":["伦敦","爱丁堡","伯明翰"]}]}
        self.example = [
                            {"北京":1,"杭州":0,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":0,"爱丁堡":1,"伯明翰":1},
                            {"北京":1,"杭州":1,"上海":0,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":1,"爱丁堡":0,"伯明翰":1},
                            {"北京":0,"杭州":0,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":0,"爱丁堡":1,"伯明翰":0},
                            {"北京":0,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":0,"爱丁堡":1,"伯明翰":1},
                            {"北京":1,"杭州":0,"上海":0,"华盛顿":1,"洛杉矶":1,"纽约":0,"伦敦":1,"爱丁堡":0,"伯明翰":1},
                            {"北京":1,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":1,"纽约":1,"伦敦":0,"爱丁堡":1,"伯明翰":0},
                            {"北京":0,"杭州":1,"上海":1,"华盛顿":0,"洛杉矶":1,"纽约":0,"伦敦":1,"爱丁堡":0,"伯明翰":1},
                            {"北京":1,"杭州":1,"上海":1,"华盛顿":1,"洛杉矶":0,"纽约":1,"伦敦":1,"爱丁堡":1,"伯明翰":0}
                        ]
        self.loop_count = [0 for _ in range(9)]
        self.cn_level_two_flag = False
        self.us_level_two_flag = False
        self.uk_level_two_flag = False
    
    def reset_variables(self):
        self.loop_count = [0 for _ in range(9)]
        self.cn_level_two_flag = False
        self.us_level_two_flag = False
        self.uk_level_two_flag = False
    
    def calculate(self):
        level_one = 0
        level_two = 0
        level_three = 0
        print(f"initialize: {self.loop_count}")

        for dict in self.example:
            count = 0
            for key in dict:
                if dict[key] == 1:
                    self.loop_count[count] = 1
                else:
                    self.loop_count[count] = 0 
                count += 1
            print(self.loop_count)

            # check CHINA
            cn_count = 0
            for i in range(0, 3):
                cn_count += self.loop_count[i]
            if cn_count == 2:
                level_three += 1
            elif cn_count == 3:
                level_three += 2
            
            if self.loop_count[0] == 1 and self.loop_count[1] == 1 and self.loop_count[2] == 1:
                level_two += 2
                self.cn_level_two_flag = True
            elif self.loop_count[0] == 1 and self.loop_count[1] == 1:
                level_two += 1
                self.cn_level_two_flag = True
            elif self.loop_count[1] == 1 and self.loop_count[2] == 1:
                level_two += 1
                self.cn_level_two_flag = True

            # check USA
            us_count = 0
            for i in range(3, 6):
                us_count += self.loop_count[i]
            if us_count == 2:
                level_three += 1
            elif us_count == 3:
                level_three += 2
            
            if self.loop_count[3] == 1 and self.loop_count[4] == 1 and self.loop_count[5] == 1:
                level_two += 2
                self.us_level_two_flag = True
            elif self.loop_count[3] == 1 and self.loop_count[4] == 1:
                level_two += 1
                self.us_level_two_flag = True
            elif self.loop_count[4] == 1 and self.loop_count[5] == 1:
                level_two += 1
                self.us_level_two_flag = True

            # check UK
            uk_count = 0
            for i in range(6, 9):
                uk_count += self.loop_count[i]
            if uk_count == 2:
                level_three += 1
            elif uk_count == 3:
                level_three += 2
            
            if self.loop_count[6] == 1 and self.loop_count[7] == 1 and self.loop_count[8] == 1:
                level_two += 2
                self.uk_level_two_flag = True
            elif self.loop_count[6] == 1 and self.loop_count[7] == 1:
                level_two += 1
                self.uk_level_two_flag = True
            elif self.loop_count[7] == 1 and self.loop_count[8] == 1:
                level_two += 1       
                self.uk_level_two_flag = True

            # check level one
            print(f"cn {self.cn_level_two_flag}, us {self.us_level_two_flag}, uk {self.uk_level_two_flag}")

            if self.cn_level_two_flag and self.us_level_two_flag and self.uk_level_two_flag:
                level_one += 2
            elif self.cn_level_two_flag and self.us_level_two_flag:
                level_one += 1                             
            elif self.us_level_two_flag and self.uk_level_two_flag:
                level_one += 1    
            # reset vars after each run
            self.reset_variables()
        
        # print final res after all runs
        print(f"一级是: {level_one}")
        print(f"二级是: {level_two}")
        print(f"三级是: {level_three}")

if __name__ == '__main__':
    run = Solution()
    run.calculate()