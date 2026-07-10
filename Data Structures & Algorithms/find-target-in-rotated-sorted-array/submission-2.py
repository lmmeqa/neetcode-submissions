class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        # [0,1,2,3,4,5]  target = 4
        # [5,6,1,2,3,4]
        # [1,2,3,4,5,6]
        # [4,5,6,1,2,3]
        # if mid is greater than right then we do an or statement of greater than mid or less than right
        # if mid is greater than left then we do 
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]:        
                if nums[l] <= target < nums[mid]:
                    r=mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


           
                
        