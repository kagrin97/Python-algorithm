import re 
def solution(files):
    
    f_split = [re.split("([0-9]+)", f) for f in files]
    # re.split는 조건에 따라 split기능을 수행한다 위식은 0~9 까지중 하나이상 나와야 성립한다      
    f_sort = sorted(f_split, key = lambda x: (x[0].lower(), int(x[1])))
    # 람다로 소문자로 파일명정렬후 숫자 정렬을 해준다
    return ["".join(f) for f in f_sort]
    # 합쳐준다


files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))