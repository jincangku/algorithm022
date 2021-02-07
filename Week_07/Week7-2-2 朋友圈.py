class Solution(object):
    def findCircleNum(self, a):
        arr=[0]*len(a)
        outlaw=0
        for x in range(0,len(a)):
            outlaw+=1
            def repeat(index,a):
                # nonlocal outlaw
                if(arr[index]>0):
                    return None
                arr[index]=outlaw
                for y in range(0,len(a[0])):
                    if(a[index][y]==1):
                        repeat(y,a)
            repeat(x,a)
        lo=[]
        for x in arr:
            if(x not in lo):
                lo.append(x)
        return len(lo)