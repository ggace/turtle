import turtle
import random
import requests


r = requests.get('https://turtle.ggace15.repl.co/turtle')
r.json()['a']

limit = 400



a_turtle = turtle.Turtle()
b_turtle = turtle.Turtle()

screen = turtle.Screen()

screen.setup(width = 1.0, height = 1.0)

turtle.hideturtle()


turtle.penup()
turtle.goto(limit, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(500)
turtle.right(180)
turtle.forward(1000)

a = r.json()['a']
b = r.json()['b']


a_list = []
b_list = []
if not(type(a) == 0 and type(b) == 0):
    temp = random.randint(0, 50)
    a = temp
    b = temp


print(a)
print(b)

for i in range(a):
    a_list.append(1)

for i in range(b):
    b_list.append(1)

    
for i in range(100-a):
    a_list.append(0)

for i in range(100-b):
    b_list.append(0)

a_turtle.penup()
a_turtle.goto(-limit, 100)

b_turtle.penup()
b_turtle.goto(-limit, -100)

text = ""

while(a_turtle.pos()[0] <= limit or b_turtle.pos()[0] <= limit):
    
    a_turtle.forward(sum(random.sample(a_list, 5)))
    b_turtle.forward(sum(random.sample(b_list, 5))) 
    if(a_turtle.pos()[0] >= limit and b_turtle.pos()[0] >= limit):
        text= "무승부"
        break
    elif(a_turtle.pos()[0] >= limit):
        text= "a가 이겼습니다."
        break
    elif(b_turtle.pos()[0] >= limit):
        text= "b가 이겼습니다."
        break

turtle.penup()
turtle.goto(0, 0)
turtle.write(text, font=("Arial", 20, "normal"))
input()
