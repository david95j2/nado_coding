print('python','java','c++', end=' ')
print('Python','java','c++', sep=' vs ')

import sys
print('python','java', file=sys.stdout)
# 로그 기록을 남길 때 사용 에러가 난 부분을 쉽게 찾을 수 있다. 
print('python','java', file=sys.stderr) 


scores = {"수학":0, "영어":50, "코딩":90}
for subject, score in scores.items():
  print(subject.ljust(8), str(score).rjust(4), sep=":")

