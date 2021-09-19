import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
menu_title = "Guess the State"

correct_answer_count = 0

data_frame = pandas.read_csv("50_states.csv")
all_states = data_frame["state"].to_list()
guessed_states = []



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = set(all_states).difference(guessed_states)
        new_data = pandas.DataFrame(missing_states)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_frame[data_frame.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)

# states to learn.csv




menu_title = correct_answer_count


