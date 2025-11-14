import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States",
        prompt="Enter a state: ").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

turtle.mainloop()
