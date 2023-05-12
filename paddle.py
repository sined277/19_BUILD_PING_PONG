from turtle import Turtle
UP = 90
DOWN = 270


class Paddple(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.goto(x_cor, y_cor)
        self.turtlesize(5, 1)
        self.shape('square')
        self.color('white')



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)



    def down(self):
        new_y = self.ycor() + -20
        self.goto(self.xcor(), new_y)







