#   天龍人的方法
def twoSum_1(self, nums: List[int], target: int) -> List[int]:
    # O(N)
    # hash lookup
    # memoization
    看過了啦 = {}
    # 看過的數字:位置
    # {3:0} 6 - 3 = 3
    # {3:0, 2:1} 6 - 2 = 4
    # {3:0, 2:1 , 4:2} 6 -4 = 2
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in 看過了啦:
            return [看過了啦[diff], i]
        else:
            看過了啦.update({nums[i]: i})
    return 看過了啦


# 客家人的方法
def twoSum_2(self, nums: List[int], target: int) -> List[int]:
    #O(N^2)
    #先照順序找第一個
    #再找第二個
    #1 + 2 == target?
    #在找第三個加第一個
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
