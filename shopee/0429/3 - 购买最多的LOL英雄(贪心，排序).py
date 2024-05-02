class Solution:
    def solution(self, costs, coins):
        costs = sorted([(c, i) for i, c in enumerate(costs)])
        selected = []
        for c, i in costs:
            if coins >= c:
                coins -= c
                selected.append((i, c))
            else:
                break

        return [c for _, c in sorted(selected)]

if __name__ == '__main__':
    costs = [2,1,3,4,5]
    coins = 10
    print(Solution().solution(costs, coins)) # [2, 1, 3, 4]
    costs = [10,5,6,11,2,3]
    coins = 10
    print(Solution().solution(costs, coins)) # [5,2,3]
    costs = [15,10,11,10]
    coins = 5
    print(Solution().solution(costs, coins)) # []