“`python

import turtle

# Tạo đối tượng turtle

t = turtle.Turtle()

# Đặt tốc độ vẽ

t.speed(10)

# Vẽ một nửa trái tim

t.penup()

t.goto(-100, 0)

t.pendown()

t.begin_fill()

t.color(“red”)

t.circle(100, 180)

t.setheading(0)

t.circle(-100, 180)

t.end_fill()

# Vẽ phần còn lại của trái tim

t.penup()

t.goto(-100, 0)

t.pendown()

t.begin_fill()

t.color(“red”)

t.circle(-100, 180)

t.end_fill()