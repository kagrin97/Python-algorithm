class Solution:
    def isPalindrome(self, x: int) -> bool:
        palin = 0
        if x == 0:
            return True
        elif x > 0:
            palin = int(str(x)[::-1])
        else:
            palin = int(str(x)[-1:0:-1])
        if x == palin:
            return True
        else:
            return False

'''
121을 거꾸로 돌려도 같은 숫자이면 true
다르면 false
음수는 무조건 false
'''