class RemoveDuplicates:
    def __init__(self, nums):
        self.nums = self.remove_duplicates(nums)

    def remove_duplicates(self, nums):
        tmp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                tmp = tmp + [nums[i]]
        
        return tmp