## Python Nado Coding Study
---
Question.

- 함수
- print 구문시 큰따옴표와 작은 따옴표 차이?
  - 문법적으로 별 차이 없음 관습임(작은 따옴표는 기호나 식별자 , 큰 따옴표는 텍스트)
    
    > but.. dictionary를 쓸때는 큰따옴표로 묶지 않으면 아래와 같은 오류를 발생한다.
  ```python
    앰퍼샌드(&) 문자를 사용할 수 없습니다. & 연산자는 나중에 사용하도록 예약되었습니다. 
    앰퍼샌드를 문자열의 일부로 전달하려면 큰따옴표로 묶으십시오("&").
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : AmpersandNotAllowed
  ```
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
    ```python
      print('python','java','c++', end=' ') # 문장의 끝 부분을 띄어쓰기 해라.
      print('Python','java','c++', sep=' vs ') # 콤마를 ' vs ' 로 바꿔라.
      # 출력 결과 : python java c++ Python vs java vs c++

      for num in range(1, 21):
        print("대기번호 : "+str(num).zfill(3))
        # zfill() 
      
      # 빈 자리는 빈공간으로 두고, 오른쪽으로 정렬을 하되, 총 10자리 공간을 확보
      print("{0: >10}".format(500))
      print("{0: >+10}".format(-500)) # 양수일때는 + 음수일때는 -
      print("{0:_<+10}".format(500)) # 왼쪽 정렬 후, 빈칸으로 _ 채우기
      print("{0:,}".format(1000000000)) # 3자리마다 콤마찍기.
      print("{0:+,}".format(1000000000)) # 3자리마다 콤마찍고 +- 부호 붙이기.
      
      # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
      # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기.
      print("{0:^<+30,}".format(100000000000))

      # 소수점 출력
      print("{0:f}".format(5/3)) 

      # 소수점 특정 자리까지 (반올림하고 출력)
      print("{:.2f}".format(5/3))
    ```
  - list
    ```python
      Best3_listType = ["덕배","아놀드","브페"]
      Best3_listType.append('더라이스') # 순서대로 입력
      Best3_listType.insert(0,'손흥민') # 특정 인덱스에 입력
      Best3_listType.pop() # 맨 뒤 index 꺼냄

      lotoo_num = [2,20,22,34,5]
      lotoo_num.sort() # 번호순정렬
      lotoo_num.reverse() # 뒤집기
      lotoo_num.clear() # 전체 삭제

      Best3_listType.extend(lotoo_num) # 리스트끼리 합치기
    ```
  - dictionary
    ```python
      rookie = {10:'홀란드', 8:'블라호비치', 12:'음바페'}
      print(rookie[12]) # 음바페 / 없을 시 프로그램 종료
      print(rookie.get(10)) # 홀란드 / 없을 시 None 으로 대체 하고 스킵함
      print(rookie.get(9, '새 유망주')) # 새 유망주 / 없을 시 새 유망주 찍음
      print(20 in rookie) # 20인 유망주가 있냐? False
      rookie[20] = "더용" # 새로운 값 추가할 때
      del rookie[12] # 키 삭제
    ```
  - tuple
    ```python
      whatThe_f = "BD33","웡크스","로셀소"
      # tuple은 값 변경 안됌.
    ```
  - set
    ```python
      # 중복이 안되고 순서가 없다.
      java = {'나', '잡스', '제프리'}
      python = set(['나', '주커버그', '빌게이츠', '머스크', '피차이'])

      # 교집합 ( java 와 python 모두 할 수 있는 사람 )
      print(java & python) 
      print(java.intersection(python))
      
      # 합집합 ( java 또는 python 할 수 있는 사람 )
      print(java | python) 
      print(java.union(python))

      # 차집합 ( java 는 할 수 있지만 python 못하는 사람 )
      print(java - python)
      print(java.difference(python))

      # python 할 줄 아는 사람 늘어남
      python.add('제프리')

      # java 를 잊음
      java.remove('잡스')
    ```
### array 겁내 중요함!!!!!!!!!!!!!!!!!!
```python
  arr = ["A","B","C","D","E","F","G","H","I","J"]
  
  # 1
  print(arr[2]) # C
  print(arr[-1]) # J
  print(arr[arr.index("F")]) # F

  # 2 slicing
  print(arr[:]) # A B C D E F G H I J
  print(arr[5:]) # F G H I J
  print(arr[-1:]) # J
  print(arr[3:7]) # D E F G
  print(arr[3:-2]) # D E F G H

  # 3 Extended Slices
  # arr[A:B:C] == index A부터 index B 까지 C의 간격으로 배열을 만들어라
  print(arr[::]) # A B C D E F G H I J
  print(arr[1::3]) # B E H  / 1번째 index 부터 3간격으로 출력
  print(arr[-5::-1]) # F E D C B A  / -5번째 idnex 부터 1간격으로 역순 출력
  print(arr[-5::1]) # F G H I J  / -5번쨰 index 부터 1간격으로 출력
  print(arr[2:6:2]) # C E  / 2번째 index 부터 6 - 1 index 까지 2의 간격으로 출력
  print(arr[-2:2:-2]) # I G E / -2번째 idnex부터 2 + 1 index 까지 -2의 간격으로 출력
```

### 클래스와 인스턴스

  - 클래스(class)는 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계, 틀과 같은 것. 
  - 객체(object)는 클래스에 의해서 만들어진 물건, 실체를 뜻한다. 
  - 클래스를 ‘자동차의 설계도’, 객체는 ‘실제로 만들어진 자동차’라고 생각하면 된다.

  - 클래스에 의해 만들어진 객체는 객체별로 독립적인 성격을 갖는다는 특징이 있다. 
  - 한 자동차의 바퀴를 바꾸거나 유리창이 깨져도 다른 자동차는 아무런 영향을 받지 않는 것과 마찬가지다. 
  - 같은 클래스에 의해 생성된 객체라도 서로에게 아무런 영향을 주지 않는다.

  - 인스턴스란 클래스에 의해 만들어진 객체이다.
  
  
  ```

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

---
#### Memo

- index() 해당 원소 찾아줌
- replace() 자바와 같음.
- input() 커서가 깜빡이면서 콘솔창에 입력하게 된다.
-
- sys.stdin   -  입력 버퍼, 입력 버퍼가 없으면 키보드 입력
- sys.stdout - 출력 버퍼, 출력 버퍼가 지정되어 있지 않으면 터미널 출력  (표준 출력)
- sys.stderr  - 출력 버퍼, 출력 버퍼가 지정되어 있지 않으면 터미널 출력 (에러 출력)
  - 출처: https://kibua20.tistory.com/71 [모바일 SW 개발자가 운영하는 블로그]

```python
  scores = {'수학':0, '영어':50, '코딩':90}
  for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
```

- with를 사용해서 close를 하지 않는다.

cf) datatype
  ```python
    a = '123' # str
    a = 123 # int
    a = 123.0 # float
    a = 12 + 3j # complex
    a = 1,2,3 # tuple
    a = {1,2,3} # set
    a = {1:1, 2:2, 3:3} # dict
    a = [1,2,3] # list
    a = set([1,2,3]) # set
  ```


cf) 전역변수 & 지역변수
  ```python
    gun = 10

    def checkpoint(soldiers):
      gun = 20
      gun = gun - soldiers
      print("[함수 내] 남은 총 : {}".format(gun))

    print("전체 총 : {}".format(gun))
    checkpoint(2)
    print("남은 총 : {}".format(gun))
  ```
  > 이렇게 진행하면 변수 gun 의 값은 변하지 않고 그대로 10이다.
  >
  > 저 gun 의 값을 변하게 하려면

  ```python
    gun = 10

    def checkpoint(soldiers):
      global gun
      gun = gun - soldiers
      print("[함수 내] 남은 총 : {}".format(gun))

    print("전체 총 : {}".format(gun))
    checkpoint(2)
    print("남은 총 : {}".format(gun))
  ```
  > 이렇게 global 이라는 전역변수를 사용하게 되면 gun의 값은 8로 변하게 된다.