class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        k=0
        s=nums.count(nums[0])
        e=nums.count(nums[-1])

        if (len(nums)-s-e)>=0:
            return len(nums)-s-e
        return 0