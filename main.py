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
states = data_frame["state"].to_list()


answer_state = screen.textinput(title=menu_title, prompt="What's another state's name?")
if answer_state in states:
    correct_answer_count = +1
else:
    print("incorrect")



