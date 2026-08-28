class Solution:
    def searchRange(self, nums, target):
        def findFirst():
            left, right = 0, len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

                if nums[mid] == target:
                    answer = mid

            return answer

        def findLast():
            left, right = 0, len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    answer = mid

            return answer

        return [findFirst(), findLast()]
