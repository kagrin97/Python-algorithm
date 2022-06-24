last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
# 전년도 성적표  생성

subjects = ["physics", "calculus", "poetry", "history"]
# 교과목 새로 생성

grades = [98, 97, 85, 88]
# 점수 생성

gradebook = list(zip(grades, subjects))
# 성적표에 교과목과 점수를 집어넣음 list를 넣어야지 나중에 print 했을시 제대로 된 값이 나옴


subjects.append("computer science")
# 과목에 컴퓨터과학 추가

grades.append(100)
# 점수에 100점 추가

gradebook.append(("visual arts", 93))
# 성적표에 직접적으로 비주얼 아트 및 93점 추가 괄호를 2번써야됨 이유는 2가지를 추가하기 때문


full_gradebook = list(zip(last_semester_gradebook + gradebook))
# 전년도와 이번년도 점수를 합침

print(full_gradebook)
