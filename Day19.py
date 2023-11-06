from turtle import Turtle, Screen
import random

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_counterclock():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
def move_clock():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward, "s")
screen.onkey(move_counterclock, "a")
screen.onkey(move_clock, "d")
screen.onkey(clear_drawing, "c")

'''is_race_on=False
screen=Screen()
colours=["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(500,400) #width=500  height=400
all_turtles=[]
i=0
for i in range(0,len(colours)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(-230,-180+70*i) #I give some space
    all_turtles.append(new_turtle)


user_bet=screen.textinput(title="Make your bet", prompt="Which turtle is gonna win the race")
print(user_bet)

if user_bet:
    is_race_on=True

while is_race_on==True:
    for current_turtle in all_turtles:
        if current_turtle.xcor()>230:
            print(f"The winner is the {current_turtle.fillcolor()} turtle.")
            if current_turtle.fillcolor()==user_bet.lower():
                print("You have won!")
            else:
                print("You have lost!")
            is_race_on=False
        current_turtle.forward(random.randint(0,10))'''










screen.exitonclick()