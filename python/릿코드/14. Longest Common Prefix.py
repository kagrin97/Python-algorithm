class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        s = strs[0]
        
        for i in range(1, len(strs)):
            tmp = ''
            for a in range(len(s)):
                try:
                    if s[a] == strs[i][a]:
                        tmp += strs[i][a]
                    else:
                        break
                except:
                    pass
            s = tmp
        
        if tmp == '':
            return ""
        return s

'''
strs안의 문자열 중에서 가장긴 공통 접두사를 출력한다
접두사가 없을경우 ''을 출력한다
문자열이 단 하나만 존재할경우 그 문자열을 통째로 출력한다
'''