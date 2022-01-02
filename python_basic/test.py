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

# class Number: 
#   def __init__(self,n): 
#     self.n = n 
# n1 = Number(3) 
# n2 = Number(4) 

# ### 위는 에러나는 전코드, 아래는 변경 코드 ### 

# class Number: 
#   def __init__(self,n): 
#     self.n = n 
#   def __add__(self, other): 
#     if isinstance(other, Number): 
#       return Number(self.n +other.n) 
#     elif isinstance(other, int): 
#       return Number(self.n + other) 
      
# n1 = Number(3) 
# n2 = Number(4) 
# print(n1+n2) # <__main__.Number object at 0x03248040> 
# print((n1+n2).n) 
# print(n1 + 3) # <__main__.Number object at 0x03248058> 
# print((n1 + 3).n)

# class Person:
#     def greeting(self):
#         print('안녕하세요.')
 
# class Student(Person):
#     def greeting(self):
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
# james = Person()
# james.greeting()
# james = Student()
# james.greeting()

class delftstack:
	def __init__(self, *args):
		if len(args)>3:
			self.ans = "More than three"
		elif len(args)<=3:
			self.ans = "Less than three"

s1 = delftstack(1,2,3,4)
print(s1.ans)

s2 = delftstack(1,2)
print(s2.ans)
