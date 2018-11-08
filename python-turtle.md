turtle.pendown() # 放下画笔 
turtle.penup() # 抬起画笔 
turtle.pensize(int) # 设置画笔宽度，值为整数型 
turtle.forward(float) # 讲话比向前移动一定的角度 
turtle.backward(float) # 将画笔向后移动一定的角度 
turtle.right(angle) # 将画笔右转一定的角度 
turtle.left(angle) # #将画笔左转一定的角度 
turtle.goto(x,y) # 将画笔移动到一个指定的绝对坐标 
turtle.setx(x) # 设置画笔向x方向移动的距离，值为实数 
turtle.sety(y) # 设置画笔向y方向移动的距离，值为实数 
turtle.setheading(angle) # 设定turtle箭头的方向为指定方向，0–东 90—北 
turtle.home() # 将画笔返回到原点 
turtle.circle(r,ext,steps=int) # 绘制一个设置半径和阶数的圆(设置之后会绘制多边形) 
turtle.dot(d,color) # 绘制一个指定直径的圆点，颜色为字符串类型 
turtle.undo() #取消最后一个图操作 
turtle.speed(s) # 设置画笔颜色，为整数类型，且取值在1-10之间 
turtle.color(‘str’) # 设置画笔颜色，为字符串类型 
turtle.fillcolor(‘str’) # 设置填充颜色，为字符串类型 
turtle.begin_fill() # 结束填充 
turtle.end_fill() # 开始填充 
turtle.filling() # 返回填充状态，True表示填充，False表示没有填充 
turtle.clear() # 清除窗口所有内容 
turtle.reset() # 清除窗口，将状态和位置复位为初始值 
turtle.screensize(w,h) # 设置turtle显示的大小，并设置宽度和高度 
turtle.hideturtle() # 隐藏turtle箭头 
turtle.showturtle() # 显示turtle窗口 
turtle.done() # 使turtle窗口不会自动消失 
turtle.isvisible() # 如果turtle可见，返回turtle 
turtle.write(‘str’,font=(“Arial”,8,”normal”)) # 在turtle位置编写字符串s，字体由字体名、字体大小、字体类型三部分组成 
turtle.position() # 获取画笔的坐标，返回一个元组，值为浮点型
--------------------- 
作者：永不—>止步 
来源：CSDN 
原文：https://blog.csdn.net/qq_38723677/article/details/82781208 
版权声明：本文为博主原创文章，转载请附上博文链接！
