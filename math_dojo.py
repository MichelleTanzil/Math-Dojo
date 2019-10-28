class MathDojo:
  def __init__(self):
    self.result = 0
  def add(self, num, *nums):
    self.result += num
    for i in nums:
      self.result += i
    return self
  def subtract(self, num, *nums):
    self.result -= num
    for i in nums:
      self.result -= i
    return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

instance_a = MathDojo()
y = instance_a.add(5).add(5,5,1,2).add(5,6,7,8,9).result
print(y)

instance_b = MathDojo()
z = instance_b.subtract(1).subtract(1,2).subtract(3,5,7).result
print(z)