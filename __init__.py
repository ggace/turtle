import turtle
import random
import requests


r = requests.get('https://turtle.ggace15.repl.co/turtle')
r.json()['a']

turtle.hideturtle()


turtle.penup()
turtle.goto(800, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(500)
turtle.right(180)
turtle.forward(1000)

a_turtle = turtle.Turtle()
b_turtle = turtle.Turtle()

screen = turtle.Screen()

screen.setup(width = 1.0, height = 1.0)

a = r.json()['a']
b = r.json()['b']

print(a)
print(b)

a_list = []
b_list = []

for i in range(a):
    a_list.append(1)

for i in range(b):
    b_list.append(1)

    
for i in range(100-a):
    a_list.append(0)

for i in range(100-b):
    b_list.append(0)

a_turtle.penup()
a_turtle.goto(-800, 100)

b_turtle.penup()
b_turtle.goto(-800, -100)

text = ""

while(a_turtle.pos()[0] <= 800 or b_turtle.pos()[0] <= 800):
    
    a_turtle.forward(sum(random.sample(a_list, 5)))
    b_turtle.forward(sum(random.sample(b_list, 5))) 
    if(a_turtle.pos()[0] >= 800 and b_turtle.pos()[0] >= 800):
        text= "무승부"
        break
    elif(a_turtle.pos()[0] >= 800):
        text= "a가 이겼습니다."
        break
    elif(b_turtle.pos()[0] >= 800):
        text= "b가 이겼습니다."
        break

turtle.penup()
turtle.goto(0, 0)
turtle.write(text, font=("Arial", 20, "normal"))
input()