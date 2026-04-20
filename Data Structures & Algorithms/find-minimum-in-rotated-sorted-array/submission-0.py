class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # minimum is to the right of mid
                l = mid + 1
            else:
                # minimum is at mid or to the left
                r = mid

        return nums[l]