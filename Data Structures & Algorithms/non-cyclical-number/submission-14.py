class Solution:
    def isHappy(self, n: int) -> bool:
        
        # while 1 <= n <= 1000:
        #     x = n%10
        #     l = l + (x**2)
        #     if l>=10:
        #         k = l%10
        #         j= l%100
        #         l = (k**2) + (j**2)
        #     n = n/10
        #     m=l
        # if (m == 1):
        #     return True
        # else:
        #     return False 
        i=0
        j=0
        if (n==1):
            return True
        while (n!=1):
            x = [0] * 4  
            l =0
            for i in range(0,4):
                x[i] = n%10
                n =n//10  
            l = x[0]**2 + x[1]**2 + x[2]**2 + x[3]**2 
            if (l ==1):
                return True
            j = j + 1
            if (j>4):
                break
            else:
                n = l     
            
        return False
