import turtle
import pandas as pd
#set up the screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
correct_guess = []

states_data = pd.read_csv("50_states.csv")

while len(correct_guess) != 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", 
                                    prompt="What's another state's name?").title()

    state_name = states_data[states_data.state == answer_state]

    if answer_state in states_data.state.values:
        t.hideturtle()
        t.penup()
        t.goto(int(state_name.x), int(state_name.y))
        t.write(answer_state)
        correct_guess.append(answer_state)


screen.exitonclick()

