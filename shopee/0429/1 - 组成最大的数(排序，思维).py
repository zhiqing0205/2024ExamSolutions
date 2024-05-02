#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param nums int整型 一维数组 
# @return string字符串
#
from functools import cmp_to_key
class Solution:
    def LargestNum(self, nums):
        # write code here
        def cmp(a, b):
            return  int(str(a) + str(b)) - int(str(b) + str(a))

        nums.sort(key=cmp_to_key(cmp), reverse=True)
        return ''.join(map(str, nums))
    

if __name__ == '__main__':
    nums = [10, 2]
    print(Solution().LargestNum(nums)) # 210
    nums = [10, 9, 8]
    print(Solution().LargestNum(nums)) # 9810