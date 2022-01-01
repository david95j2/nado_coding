# # 연산자 오버로딩 예제 1 
# class NumBox: 
#   def __init__(self,num): 
#     self.num = num 
#   def __add__(self, num): 
#     self.num += num 
#   def __sub__(self, num): 
#     self.num -= num 

# n = NumBox(40) 

# n + 100 # n+100 == n.__add__ 
# print(n.num) 

# n-100 
# print(n.num)

class Calculator:
  def __init__(self,num):
    self.num = num
  def __add__(self, num):
    self.num += num
  def __sub__(self, num):
    self.num -= num

n = Calculator(40)

n + 100
print(n.num)

n-100
print(n.num)