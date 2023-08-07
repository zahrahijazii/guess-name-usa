import turtle
import pandas as pd
import csv
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

    if answer_state == "Exit":
        all_states = states_data.state.to_list()
        missing_states = []
        for state in all_states:
            if state not in correct_guess:
                missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

    elif answer_state in states_data.state.values:
        t.hideturtle()
        t.penup()
        t.goto(int(state_name.x), int(state_name.y))
        t.write(answer_state)
        correct_guess.append(answer_state)








