class Solution:
    def ReverseString(self, originStr):
        return ' '.join([str[::-1] for str in originStr.split(' ')])
    
if __name__ == '__main__':
    originStr = "hello world, my friends"
    solution = Solution()
    print(solution.ReverseString(originStr))