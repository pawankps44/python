class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def pointfallsinrect(self,rectangle):
        if(rectangle.lowleft.x<point1.x<rectangle.upright.x and rectangle.lowleft.y<point1.y<rectangle.upright.y):
            print('true')
            return True
            # print('true')
        else:
            print('false')
            return False

class Rectangle:

    def __init__(self,lowleft,upright):
        self.lowleft = lowleft
        self.upright = upright

rectangle= Rectangle(Point(int(input("low left =" )),int(input("low right ="))),Point(int(input("up left =" )),int(input("up left ="))))

point1 = Point(int(input("x coordinate =" )),int(input("y coordinate =")))
print("x",type(point1.x))
print("y",point1.y)
point1.pointfallsinrect(rectangle)
# print(point1.x)