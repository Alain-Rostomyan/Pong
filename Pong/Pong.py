import turtle
import one_player
import two_player

# Set up a window
screen = turtle.Screen()
screen.title("Pong -- Alain, Millan, Alienor, Toscane")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)  # Turn on manual updates of the screen -> Makes the game quicker

# Create the title and choose mode texts
welcome_text = turtle.Turtle()
welcome_text.color("white")
welcome_text.penup()
welcome_text.hideturtle()
welcome_text.goto(0, 100)
welcome_text.write("Welcome to Pong", align="center", font=("Courier", 24, "normal"))

mode_text = turtle.Turtle()
mode_text.color("white")
mode_text.penup()
mode_text.hideturtle()
mode_text.goto(0, 35)
mode_text.write("Click to choose a mode:", align="center", font=("Courier", 18, "normal"))

two_player_text = turtle.Turtle()
two_player_text.color("white")
two_player_text.penup()
two_player_text.hideturtle()
two_player_text.goto(0, -20)
two_player_text.write("Two Player", align="center", font=("Courier", 18, "normal"))

ai_text = turtle.Turtle()
ai_text.color("white")
ai_text.penup()
ai_text.hideturtle()
ai_text.goto(0, -60)
ai_text.write("AI Mode", align="center", font=("Courier", 18, "normal"))

w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False


# Function to handle clicks on the screen
state = "menu"


def on_click(x, y):
    """
    Handle mouse clicks in the game window.

    This function is designed to respond to mouse clicks during the game's menu state.
    If the click falls within specific text bounding boxes on the menu screen,
    it triggers corresponding actions to transition to different game modes.

    Parameters:
    - x (float): The x-coordinate of the mouse click.
    - y (float): The y-coordinate of the mouse click.

    Global Variables:
    - state (str): The current state of the game ("menu" or "playing").

    Actions:
    - If the game is in the "menu" state and the click is within the "Two Player" text bounding box:
        - Clear the menu elements
        - Set up the game for two players
        - Transition to the "playing" state
    - If the game is in the "menu" state and the click is within the "AI Mode" text bounding box:
        - Clear the menu elements
        - Set up the game for one player against AI
        - Transition to the "playing" state
    """
    global state
    if state == "menu":
        if -70 < x < 70 and -15 < y < 5:  # Click within the "Two Player" text bounding box
            # Clear window
            welcome_text.clear()
            mode_text.clear()
            two_player_text.clear()
            ai_text.clear()

            # Set up the game for two players
            state = "playing"
            two_player.setup_2_players()
        elif -150 < x < 140 and -55 < y < -35:  # Click within the "AI Mode" text bounding box
            # Clear landing page
            welcome_text.clear()
            mode_text.clear()
            two_player_text.clear()
            ai_text.clear()

            # Set up the game for one player
            state = "playing"
            one_player.setup_1_player()


# Bind click events to screen
screen.onscreenclick(on_click)

# Update the screen
screen.update()

# Listen for click events
turtle.mainloop()
