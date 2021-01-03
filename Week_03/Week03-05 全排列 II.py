class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        output = permutations(nums, len(nums))
        output = set(output)
        output = list(output)
        return output
