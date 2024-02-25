import turtle
import random
import time
import math

window = turtle.Screen()
window.bgcolor("white")
window.register_shape("dino.gif")
windo = turtle.Screen()
windo.register_shape("cloud.gif")
wind = turtle.Screen()


size_of_barrierX = [3, 3.6, 3.2, 3.3, 2.6, 2.5,2,2.8,3.2, 2.1, 3.4, 2.25, 2.6,2.5,2.8 ]
size_of_barrierY = [4, 4.8, 4.2, 4.3, 4.6, 4.5,4.1,4.4 , 5.2, 4.9, 4.7, 5.1, 4.3, 5.4,4.6,5.1]

a = 0
score = 0

base= turtle.Turtle()
base.color("grey")
base.speed(0)
base.penup()
base.setposition(100, -300)
base.shape("square")
base.shapesize(10, 100)

cl = turtle.Turtle()
cl.color("grey")
cl.speed(0)
cl.penup()
cl.setposition(200, 180)
cl.shape("cloud.gif")

obstacle = turtle.Turtle()
obstacle.color("black")
obstacle.speed(0)
obstacle.penup()
a = random.randint(-300, 400)
obstacle.setposition(a, -151)
obstacle.shape("square")
obstacle.shapesize(random.choice(size_of_barrierY), random.choice(size_of_barrierX ))

obstacles = turtle.Turtle()
obstacles.color("black")
obstacles.speed(0)
obstacles.penup()
a = random.randint(-300, 800)
obstacles.setposition(a, -151)
obstacles.shape("square")
obstacles.shapesize(random.choice(size_of_barrierY), random.choice(size_of_barrierX ))


changex = 24

dino= turtle.Turtle()
dino.speed(0)
dino.penup()
dino.setposition(-592, -151)
dino.shape("dino.gif")
dino.setheading(90)
dino.state = "ready"
chanx = 0.9
dy = 40

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.penup()
pen.setposition(-190, 300)
pen.write("Score: ", font=("Arial", 20, "bold"))

pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.penup()
pen1.speed(0)
pen1.penup()
pen1.setposition(-280, 302)
pen1.write("Score: ", font=("Arial", 20, "bold"))

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.speed(0)
pen2.penup()
pen2.setposition(10, 52)


def jump():
   if dino.state == "ready":
      dino.forward(240)
      dino.state = "jumping"

turtle.listen()
turtle.onkey(jump, "space")
speed = 1

i = 0
def collision():
   global dist,dist1
   dist = math.sqrt((dino.xcor() -obstacle.xcor())**2+(dino.ycor() -obstacle.ycor())**2)
   dist1 = math.sqrt((dino.xcor() -obstacles.xcor())**2+(dino.ycor() -obstacles.ycor())**2)
   return dist,dist1
time.sleep(1)
while True:
      
     if dino.ycor() == -151:
         dino.state = "ready"
     pen1.write("Score:",font=("Arial", 20, "bold"))
     pen.clear()
     score+=2
     pen.write( "{}".format(score),font=("Arial", 20, "bold"))
     a+=1
     y = obstacle.xcor()
     y  = y - changex
     obstacle.setx(y)

     w = obstacles.xcor()
     w  = w - changex
     obstacles.setx(w)
     
     pos = collision()
     if int(pos[0]) < 20 or int(pos[1]) < 20:
        pen2.write("Game Over! ", font=("Arial", 40, "bold"))
        break
         
     
     if dino.ycor() > -151:
        y = dino.ycor()
        y = y - dy
        dino.sety(y)
     elif dino.ycor() <-151:
        dino.sety(-151)
        
     else:
        speed = 0
        dino.backward(speed)
     if obstacle.xcor() < -700 :
         a = random.randint(0, 650)
         obstacle.shapesize(random.choice(size_of_barrierY), random.choice(size_of_barrierX ))
         obstacle.setposition(a, -152)
         
     if obstacles.xcor() < -700 :
         b = random.randint(100, 1050)
         obstacles.shapesize(random.choice(size_of_barrierY), random.choice(size_of_barrierX ))
         obstacles.setposition(b, -152)
      
     if score == 102:
        changex = 30
        window.bgcolor("#76fbf7")
         
     if score == 702:
         window.bgcolor("black")
         obstacle.color("white")
         pen.color("white")
         pen1.color("white")
     if score == 1002:
         window.bgcolor("white")
         obstacle.color("black")
         pen.color("black")
         pen1.color("black")
     flag = False
     if score > 200:
        dy =  50

    
   