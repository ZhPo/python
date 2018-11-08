import turtle as t
def curvemove():#曲线函数
    for i in range(200):
        t.right(1)
        t.forward(1)
t.color('red','pink')
t.begin_fill()
t.left(140)
t.forward(111.65)
curvemove()
t.left(120)
curvemove()
t.forward(111.65)
t.end_fill()
t.done()
#begin_fill与end_fill之间为主要代码
----------------------------------------
import turtle as t
t.pensize(2)
t.color("red","pink")
t.begin_fill()
t.left(45)
t.fd(200)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)
t.fd(200)
t.end_fill()
t.done()
