class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
                return False

        temp = 0
        while x > temp:
            mod = x % 10
            x= (x-mod)/10
            if(x <= temp):
                break
            temp = temp *10 + mod
        
        if x == temp:
            return True
        else:
            return False
