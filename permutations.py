from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    used = [False] * n

    def helper(path):
        if len(path) == n:
            res.append(path.copy())
            return
        
        for i in range(n):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            helper(path)

            path.pop()
            used[i] = False

    helper([])
    return res

#     []
#   /  |  \
# 1a  1b   2
def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []
    path = []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # Skip duplicates on the same level
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])

            dfs()

            path.pop()
            used[i] = False

    dfs()
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))

    nums = [1, 1, 2]
    print(permute(nums))
    print(permuteUnique(nums))