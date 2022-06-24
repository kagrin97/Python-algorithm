class Solution:
    def romanToInt(self, s: str) -> int:
        roma = dict()
        roma['I'] = 1
        roma['V'] = 5
        roma['X'] = 10 
        roma['L'] = 50
        roma['C'] = 100
        roma['D'] = 500
        roma['M'] = 1000
        result = 0
        tmp = 0
        for i in range(len(s)):
            if roma[s[i]] <= tmp:
                result += roma[s[i]]
            else:
                result -= tmp
                result += roma[s[i]] - tmp
            tmp = roma[s[i]]
        return result
        
'''
s = 'III'일경우 답은 3이다
만약 IV 는 6이라고 생각하기 쉽지만 4이다 왜냐하면
현재 숫자보다 앞숫자가 작을경우 현재숫자 - 전숫자 를 더해줘야하기
때문이다
'''