def solution(numbers):
    answer = []

    for i in range(len(numbers)):
      x = numbers[i]
      tmp_x = numbers[i]
      two_x = format(x, 'b')
      while 1:
        tmp_x += 1
        two_tmp = format(tmp_x, 'b')

        if len(two_x) != len(two_tmp):
          while 1:
            if len(two_x) == len(two_tmp):
              break
            elif len(two_x) > len(two_tmp):
              two_tmp = '0' + two_tmp
            elif len(two_x) < len(two_tmp):
              two_x = '0' + two_x
        
        cnt = 0
        for k in range(len(two_x)):
          if two_tmp[k] != two_x[k]:
            cnt += 1
        if cnt <= 2:
          answer.append(tmp_x)
          break

        
    return answer

numbers = [2,7]
print(solution(numbers))