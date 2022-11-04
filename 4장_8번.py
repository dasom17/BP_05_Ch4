Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t.screen.exitonclick()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t.screen.exitonclick()
NameError: name 't' is not defined
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> lista = []
>>> lista.append(int(input("x1: ")))
x1: 0
>>> lista.append(int(input("y1: ")))
y1: 0
>>> lista.append(int(input("x2: ")))
x2: 100
>>> lista.append(int(input("y2: ")))
y2: 100
>>> lista.append(int(input("x3: ")))
x3: 200
>>> lista.append(int(input("y3: ")))
y3: 200
>>> goto(lista[0], lista[1])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    goto(lista[0], lista[1])
NameError: name 'goto' is not defined
>>> t.goto(lista[0], lista[1])
>>> t.goto(lista[2], lista[3])
>>> t.goto(lista[4], lista[5])
>>> t.screen.exitonclick()
>>> 
