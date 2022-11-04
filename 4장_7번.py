Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> lista = [ ]
>>> color = input("색상 #1을 입력하시오: ")
색상 #1을 입력하시오: yellow
>>> lista.append(color)
>>> color = input("색상 #2를 입력하시오: ")
색상 #2를 입력하시오: red
>>> lista.append(color)
>>> color = input("색상 #3을 입력하시오: ")
색상 #3을 입력하시오: blue
>>> lista.append(color)
>>> t.fillcover(lista[0])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t.fillcover(lista[0])
AttributeError: 'Turtle' object has no attribute 'fillcover'
>>> t.fillcolor(lista[0])
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> t.up()
>>> t.goto(100,0)
>>> t.down()
>>> t.fillcolor(lista[1])
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> 
KeyboardInterrupt
>>> t.up()
>>> t.goto(200,0)
>>> 
KeyboardInterrupt
>>> t.down()
>>> t.fillcolor(lista[2])
>>> t.begin_fill()
>>> t.circle(50)
>>> t.end_fill()
>>> t.screen.exitonclick()
