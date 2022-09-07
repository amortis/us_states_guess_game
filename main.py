import turtle
import pandas


def up_first_letter(word):
    new_word = ''
    for i in range(len(word)):
        if i == 0:
            new_word += word[0].upper()
        else:
            new_word += word[i]
    return new_word


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = {}
name_of_states = []
with open("50_states.csv") as file:
    data = pandas.read_csv(file)
    for i in range(len(data)):
        state = data["state"][i]
        name_of_states.append(state)
        x = data["x"][i]
        y = data["y"][i]
        cor = [x, y]
        states[state] = cor
lower_name_of_states = list(map(lambda item: item.lower(), name_of_states))
states_on_map = []
for state in name_of_states:
    cor = states[state]
    x = cor[0]
    y = cor[1]
    new_state = turtle.Turtle(visible= False)
    new_state.penup()
    new_state.goto(x, y)
    states_on_map.append(new_state)
screen.update()

game_is_on = True
guess_count = 0
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")

while game_is_on:
    if guess_count == 1:
        screen.textinput(title="Congratulations!", prompt="You completed the game and guessed all 50 states of US!"
                                                          " Tap 'Ok' to close the game")
        screen.bye()
    if answer_state.lower() in lower_name_of_states:
        guess_count += 1
        cur_state_num = lower_name_of_states.index(answer_state.lower())
        cur_state = states_on_map[cur_state_num]
        cur_state.write(up_first_letter(answer_state.lower()))
        answer_state = screen.textinput(title=f"State's guessed: {guess_count}/50", prompt="What's another state's name")
    else:
        answer_state = screen.textinput(title=f"State's guessed: {guess_count}", prompt="What's another state's name")
