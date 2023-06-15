from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width= 500,height = 400)
colors = ["red", "orange","yellow","green","blue","purple"]
y_positions= [-70,-40,-10,20,50,80]
y_position = -100
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color((colors[i-1]))
    new_turtle.goto(-230,(y_positions[i-1]))
    all_turtles.append(new_turtle)
    #new_turtle.append(all_turtles)

user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")

def race():
    global game_on
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor()>=230:
            game_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You got it right! The {winner} turtle is the winner!")
                return
            else:
                print(f"You lose. The {winner} turtle is the winner!")
                return

game_on = True

while game_on ==True:
    race()





game_on = True



screen.exitonclick()