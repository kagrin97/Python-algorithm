import re 
def solution(files):
    
    f_split = [re.split("([0-9]+)", f) for f in files]
            
    f_sort = sorted(f_split, key = lambda x: (x[0].lower(), int(x[1])))

    return ["".join(f) for f in f_sort]



files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))