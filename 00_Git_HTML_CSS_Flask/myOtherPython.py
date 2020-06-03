from myPython import square

print(square(10))

class Point: #defines the class
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(3,5) #create an object
print(p.x)
print(p.y)
