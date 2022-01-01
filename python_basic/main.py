# class Smartphone:
# 	# Smartphone class
	
#   def __init__(self, brand, informations):
#     self._brand = brand
#     self._informations = informations

#   def __str__(self):
#     return f'str : {self._brand} - {self._informations}'

#   def __repr__(self):
#     return f'repr : {self._brand} - {self._informations}'
    

# Smartphone1 = Smartphone('Iphone', {'color' : 'White', 'price': 10000})
# Smartphone2 = Smartphone('Galaxy', {'color' : 'Black', 'price': 8000})

# print(Smartphone1)
# print(Smartphone1.__dict__)

# print(Smartphone1._brand == Smartphone2._brand)
# print(Smartphone1 is Smartphone2)

# print(Smartphone.__doc__)   

a = open("test.txt","r",encoding="utf-16")
print(a.readline(), end="")