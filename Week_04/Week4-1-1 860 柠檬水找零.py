class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        remaining = {5: 0, 10: 0, 20: 0}
        for element in bills:
            if element == 5:
                remaining[element] += 1
            elif element == 10:
                remaining[element] += 1
                if remaining[5] == 0:
                    return False
                else:
                    remaining[5] -= 1
            else:
                remaining[element] += 1
                if (remaining[10] != 0) and (remaining[5] != 0):
                    remaining[10] -= 1
                    remaining[5] -= 1
                elif remaining[5] >= 3:
                    remaining[5] -= 3
                else:
                    return False
        return True
