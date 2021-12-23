## Python Nado Coding Study
---
Question.

- 함수
- print 구문시 큰따옴표와 작은 따옴표 차이?
  - 문법적으로 별 차이 없음 관습임(작은 따옴표는 기호나 식별자 , 큰 따옴표는 텍스트).
- 

---
---

### 특징

1. Java와 달리 변수를 선언할 때, 자료형을 명시적으로 선언하지 않는다 

```java
// java 에서의 변수 선언
  int num = 10
  printf("int num = %d\n", num);
```

```python
# Python 에서의 변수 선언
  num = 10
  print("int num = %d" %num)
```

2. print 구문시 

```python
# 첫번째 방법
name = "손흥민"
print('name = '+name) # 출력 결과  name = 손흥민

# 두번째 방법 콤마로 할 시 앞에 뛰어쓰기 한칸 생김
print('name = ',name) # 출력 결과  name =  손흥민 
```

---
### DataType

1. 수치자료형
  - int
  - float
  - complex

2. bool 자료형
  - boolean

3. 군집 자료형
  - str
  - list
  - tuple
  - set
  - dictionary



### 연산자

```python
  print(2**3) # 2^3 = 8
  print(5%3) # 나머지 = 2
  print(7//3) # java와 달리 슬래시 두번!! 몫 = 2

  # 같다 표시 = 두번
  print(10==10) # True
    
  # 다름
  print(10!=10) # False
  print(not( 1!= 3)) # False
    
  # and &
  print((3>0) and (3<5)) # True
  print((3>0) & (3<5)) # True

  # or |
  print((3>0) or (3>5)) # True
  print((3<0) | (3>5)) # False
```

### 숫자처리 함수
```python
print(abs(-5)) #5 절대값
print(pow(4, 2)) # 4^2 제곱
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림
print(celi(3.14)) # 올림
print(sqrt(16)) # 제곱근 4
```


### 랜덤함수

```python
from random import *
print(random()) # 0.0 이상 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 ~ 10 이하의 임의의 값 생성

# 로또 번호 추첨시
print(int(random() * 45) + 1) # 1 이상 ~ 45 이하의 임의의 값 생성
# 로또 번호 추첨시 randrange 방법
print(randrange(1,46)) # 1 이상 ~ 45 이하의 임의의 값 생성 46은 포함안됌!!!!!!!!!!!!!
# 로또 번호 추첨시 randint 방법
print(randint(1,45)) # 1 이상 ~ 45 이하의 임의의 값 생성
```

#### Quiz )
```python
import random
print('오프라인 스터디 모임 날짜는 매월',str(random.randint(4,28))+'일로 선정되었습니다.')
```


### 문자열 포맷
```python
print("손흥민이 리그에서 %d골 박고 %s 발랐으면 좋겠다. when the %cpurs go marching in!!" % (3, "맨유", "s"))
#출력 결과 : 손흥민이 리그에서 3골 박고 맨유 발랐으면 좋겠다. when the spurs go marching in!!


print("{1}랑 {0}도 {2}골 차이로 이길 수 있다고 믿습니다.. 콘버지.. {3}좀 버려라.." .format("첼시", "리버풀", 2, "bd33 "))
#출력 결과 : 리버풀랑 첼시도 2골 차이로 이길 수 있다고 믿습니다.. 콘버지.. bd33 좀 버려라..

print("만약 \"{rival}\"한테 {goal}골 이라도 먹히면 다 죽는거야.." .format( goal = 1,rival = "아스널"))
#출력 결과 : 만약 "아스널"한테 1골 이라도 먹히면 다 죽는거야..

name = "덕배"
age = 26
print(f"{age}살 '{name}'가 살아나니 겁나 좋다")
#출력 결과 : 26살 '덕배'가 살아나니 겁나 좋다
```

#### Quiz )
```python
site = "https://naver.com"
site = site.replace("https://","")
site = site[:site.index(".")]
site = site[:3]+str(len(site))+str(site.count("e")) + "!"
print(site)
```