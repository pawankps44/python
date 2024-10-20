import numpy as np
from PIL import Image

class Square:
    def __init__(self,x,y,length,colour):
        self.x = x
        self.y = y
        self.length = length
        self.colour = colour

    def draw(self):
        canvas.data[self.x:self.x+self.length,self.y:self.y + self.length] = self.colour

class Rectangle:
    def __init__(self,x,y,height,length,colour):
        self.x = x
        self.y = y
        self.length = length
        self.colour = colour
        self.height = height

    # def draw(self):

class Canvas:
    def __init__(self,x,y,colour):
        self.x = x
        self.y= y
        self.colour = colour
        self.data = np.full((self.x,self.y,3),self.colour,dtype=np.uint8)


    def save(self,filename):
        img = Image.fromarray(self.data,'RGB')
        img.save(filename)

canvas = Canvas(200,200,(255,255,255))
sq = Square(20,20,20,(255,255,0))
sq.draw()
canvas.save("canvas.png")


