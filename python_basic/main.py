arr = ["A","B","C","D","E","F","G","H","I","J"]
# print(arr[::2])
# print(arr[1::2])

# arr_num = [1,2,3,4,5,6,7,8,9,10]
# print(arr[3::-1])
a = list(input())
print(a)

# for i in a:
#       print("Case #{}:  "+eval(input().replace(" ","+")).format(str(i)))


class Parents:
  # 메소드
  def __init__(self, name, age):
    # 이것이 멤버변수
    self.name = name
    self.age = age
    print('초기화')

  def home(self, locataion):
    print("{}는 {}살이며, {}에 사신다.".format(self.name,self.age,locataion))  

# 이것이 객체
father = Parents('아버지','대전')

mother = Parents('어머니','세종')

#확장된 변수는 할당한 객체에만 적용된다.
mother.child = True


