import turtle
import pandas

screen = turtle.Screen()         # Setting up the turtle screen
screen.title("U.S. States Game")
image  = "blank_states_img.gif"  # This is the path to our image file
screen.addshape(image)           # Here we are adding shape to our screen, the shape is default image
turtle.shape(image)

data           = pandas.read_csv("50_states.csv")  # saving all the data which we are reading from csv into var called 'data'
all_states     = data.state.to_list()              # We should convert the data into list just to use the 'in' keyword to traverse while checking
guessed_states = []                                # to keep track of how many states the user guessed and storing it in this list

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()  # The title case is to make first letter capital
    # print(answer_state)
    if answer_state == "Exit".title():
        missing_states = [state for state in all_states if state not in all_states]  # List comprehension used
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


    if answer_state in all_states:

        guessed_states.append(answer_state)           # appending the newly added states to the list
        t = turtle.Turtle()                           # turtle is a library and Turtle is a class within that library
        t.hideturtle()
        t.penup()                                     # this is to avoid the turtle doing any drawing or creating lines on the screen while movement
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))  # Converting the data into int as they are formatted in string already
        t.write(answer_state)                         # item looks at underlying data and takes first element

screen.exitonclick()



# The below function takes two parameters x and y as inputs and prints it out

def get_mouse_click_coor(x,y):

    print(x,y)

# On Screen click is a event listener and whenever the mouse is clicked it calls the get_mouse... function
# which passes over the x and y on that clicked location

turtle.onscreenclick(get_mouse_click_coor)

# The turtle.mainloop() is the alternative way to keep our screen open even though our code has finished running
# So it's basically an alternative to our screen.exitonclick()

turtle.mainloop()











screen.exitonclick()