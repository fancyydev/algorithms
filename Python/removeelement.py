class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p = len(nums) - 1
        p1 = 0

        while p1 <= p:
            if nums[p] != val:
                if nums[p1] == val:
                    nums[p1] = nums[p]
                    nums[p] = '_'
                    p -= 1
                
                p1 += 1
            else: 
                nums[p] = '_'
                p-=1

        return nums
    
a = [1]
solution = Solution()

print(solution.removeElement(a,1))