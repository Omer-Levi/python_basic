"""
Student: Omer levi
ID: 203499090
Assignment no. 5
Program: intersection.py
"""


class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return (f"(X={self.__x}, Y={self.__y})")
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.y = value
    
class Line:
    def __init__(self, p, q):
        self.__p = p
        self.__q = q
    def __str__(self):
        return (f"P = {self.__p},  Q = {self.__q}")
    @property
    def p(self):
        return self.__p
    @property
    def q(self):
        return self.__q
    
    def slope(self):
        s = (self.__p.y - self.__q.y) / (self.__p.x - self.__q.x)
        return s
    
    def y_intercept(self):
        m = self.slope()
        return self.__p.y - m * self.__p.x
    
    def isParallel(self, line):
        return self.slope() == line.slope()

def main():
    x = float(input('enter x point:'))
    y = float(input('enter y point:'))
    point_1 = Point(x,y)
    x = float(input('enter x point:'))
    y = float(input('enter y point:'))
    point_2 = Point(x,y)
    x = float(input('enter x point:'))
    y = float(input('enter y point:'))
    point_3 = Point(x,y)
    x = float(input('enter x point:'))
    y = float(input('enter y point:'))
    point_4 = Point(x,y)
    line_1 = Line(point_1, point_2)
    line_2 = Line(point_3, point_4)
    print(f'line 1: {line_1}')
    print(f'line 2: {line_2}')
    print(f'the slope line 1 this {line_1.slope()}')
    print(f'the slope line 2 this {line_2.slope()}')
    print(f'the line 1 y intercept {line_1.y_intercept()}')
    print(f'the line 2 y intercept {line_2.y_intercept()}')
    if line_1.isParallel(line_2): 
        print('yes is parallel')
    else:
        print('not parallal')
     
main()
        
        

    
