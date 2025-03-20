import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')
t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('blue')
t.write( "Background color", font=('Arial',30,'bold'),align='center')
t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write( "1. Tan", font=('Arial',20,'bold'),align='left')
t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Azure')
t.write( "2. Azure", font=('Arial',20,'bold'),align='left')
t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write( "3. Aquamarine", font=('Arial',20,'bold'),align='left')
t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('darkkhaki')
t.write( "4.  darkkhaki", font=('Arial',20,'bold'),align='left')

t.penup()
t.goto(0, -100)
t.pendown()
t.pencolor('blue')
t.write( "Choose a color", font=('Arial',20,'bold'),align='center')


choose=int(input(""))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamerine')
else:
    screen.bgcolor('darkkhaki')
t.clear()

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor('black')
t.write("Enter your name", font=('Arial', 30, 'normal'), align='center')











name= input("Enter your name")
t.clear()
#num1 = int(input("Enter a number: "))
#num2 = int(input("enter a another number: "))
operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    #add
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1+num2

elif operation == 2:
    #subtract
    symbol = "-"
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1 - num2

elif operation == 3:
    #multiply
    symbol = "*"
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)

    solution = num1 * num2

elif operation == 4:
    # division
    symbol = "/"
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign = random.randint(1, 2 )
    if sign == 2:
            num2= -2*num2

    solution = num1 / num2



t.penup()
turtle.goto(0,100)
turtle.pendown()
t.pencolor('blue')
t.write( "name", font=('Arial',30,'bold'),align='center')

t.penup()
turtle.goto(-200,0)
turtle.pendown()
t.pencolor('green')
t.write( "num1", font=('Arial',30,'bold'),align='center')

t.penup()
turtle.goto(-100,0)
turtle.pendown()
t.pencolor('red')
t.write(symbol, font=('Arial',30,'bold'),align='center')

t.penup()
turtle.goto(0,0)
turtle.pendown()
t.pencolor('hot pink')
t.write( "num2", font=('Arial',30,'bold'),align='center')

t.penup()
turtle.goto(100,0)
turtle.pendown()
t.pencolor('red')
t.write( "=", font=('Arial',30,'bold'),align='center')

ans=int(input("Please enter your answer: "))

t.penup()
turtle.goto(0,-100)
turtle.pendown()
t.pencolor('black')
t.write( "Your answer is: "+str(ans), font=('Arial',30,'bold'),align='center')


# num1 = int(
num1 = random.randint(-100,100)
num2 = random.randint(-100,100)

sum = num1 + num2
ans = float(input("please enter your anwser , "))








t.penup()
turtle.goto(0,0)
turtle.pendown()
t.pencolor('purple')
t.write( "solution", font=('Arial',30,'bold'),align="center")







if ans == solution:
    screen.bgcolor('dodgerblue')
    t.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    t.pencolor('black')
    t.write("Correct", font=('Arial', 30, 'bold'), align='center')

else:
    screen.bgcolor('darkorange')

    t.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    t.pencolor('black')
    t.write("incorrect", font=('Arial', 30, 'bold'), align='center')







turtle.done()
#this is the last line of code

















































































































































































































































































































































































































































































































































































































































































































































