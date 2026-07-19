#Decorators
def my_decorator(func):
   def wrapper(*args, **kwargs):
    
    print ("Before execution")
    result = func(*args, **kwargs)
    print("After execution")
    return result
   return wrapper
@my_decorator
def add(a,b):
  return a + b
print(add(5,3))

#Iterators
class My_nums:
  def __iter__ (self): 
    self.a = 1
    return self
  def __next__ (self):
    x= self.a
    self.a +=1
    return x
My_class = My_nums()
My_iter = iter(My_class)

print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))

#Generators
def func(max):
  count =1
  while count<= max:
    yield count
    count += 1

ctr = func(10)
for n in ctr:
  print(n)