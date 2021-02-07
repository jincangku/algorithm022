class Solution(object):
    def hammingWeight(self, n):
	bstr = bin(n)[2:] # int to bit string
	return len(re.sub('[^1]', '', bstr)) # filter out 0