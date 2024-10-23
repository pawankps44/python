class Point:
    def __init__(self, x, y):
        print('hey')
        self.x = x
        self.y = y

    def Distance(self, p, q):
        print('hi')
        a = self.x - p
        b = self.y - q
        print(a, b)
        return a - b

point1 = Point(10, 7)
result = point1.Distance(3,8)
print("Result:", result)
print('hi')