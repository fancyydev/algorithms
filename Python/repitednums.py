class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        p1 = len(nums)-1
        while p < p1:
            numero_analizado = nums[p]
            print(nums)
            if nums [p + 1] == numero_analizado:
                for i in range(p,p1,1):
                    nums[i] = nums[i+1]
                p1 -= 1
            else:
                p += 1

        return nums
    
    def removeDuplicatesWithoutOrdering(self, nums: list[int]) -> int:
        if not nums:
            return 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[p]:
                p += 1  
                nums[p] = nums[i]  
        return p + 1
                    
    
a = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()

print(solution.removeDuplicates2(a))