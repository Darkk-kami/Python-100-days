import turtle
import pandas
from marker import Marker

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

score = 0
guessed_state = []

game_on = True
while game_on:

    answer_state = screen.textinput(title=f"Guess the state: {score}/50", prompt="What's another state name?").title()

    if answer_state in state_list and answer_state not in guessed_state:
        state_index = state_list.index(answer_state)
        valid_state = data[data.state == answer_state]
        valid_state_x_cor = valid_state.x[state_index]
        valid_state_y_cor = valid_state.y[state_index]
        marker = Marker(answer_state)
        marker.mark_state(x=valid_state_x_cor, y=valid_state_y_cor)
        guessed_state.append(answer_state)
        score += 1

    elif answer_state == 'Exit':
        missing_states = [state for state in state_list if state not in guessed_state]
        final_data = pandas.DataFrame(missing_states)
        final_data.to_csv("missing states.csv")
        break

    if score == 50:
        game_on = False

turtle.mainloop()


