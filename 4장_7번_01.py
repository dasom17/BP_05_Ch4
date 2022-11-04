Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> shape("turtle")
>>> lista = []; color = input("색상 #1을 입력하시오: ")
색상 #1을 입력하시오: yellow
>>> lista.append(color) = input("색상 #2를 입력하시오: ")
SyntaxError: can't assign to function call
>>> lista.append(color); = input("색상 #2를 입력하시오: ")
SyntaxError: invalid syntax
>>> lista.append(color); color = input("색상 #2를 입력하시오: ")
색상 #2를 입력하시오: red
>>> lista.append(color); color = input("색상 #3을 입력하시오: ")

색상 #3을 입력하시오: blue
>>> lista.append(color)
>>> fillcolor(lista[0]); begin_fill(); circle(50); end_fill()
>>> up(); goto(100,0); down(); fillcolor(lista[1]); begin_fill(); circle(50); end_fill()
>>> up(); goto(200,0); down(); fillcolor(lista[2]); begin_fill(); circle(50); end_fill()
>>> write("닫으려면 화면 클릭"); exitonclick()
>>> 
