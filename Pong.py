import turtle
import random

# Set up a window
window = turtle.Screen()
window.title("Pong -- Alain, Millan, Alienor, Toscane")
window.bgcolor("black")
window.setup(width=800, height=400)
window.tracer(0) #Turn on manual updates of the screen -> Makes the game quicker
### Could we make it bigger ?

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

### Are we sure about this ?
ai_text = turtle.Turtle()
ai_text.color("white")
ai_text.penup()
ai_text.hideturtle()
ai_text.goto(0, -60)
ai_text.write("AI Mode", align="center", font=("Courier", 18, "normal"))


def setup_2_players():
    # Set up the window
    window = turtle.Screen()
    window.title("Pong-- Alain, Millan, Alienor, Toscane")
    window.bgcolor("black")
    window.setup(width=600, height=400)
    ###again, bigger ?

    # Create paddles and ball
    # Player 1 paddle
    player1_paddle = turtle.Turtle()
    player1_paddle.shape("square")
    player1_paddle.color("white") 
    player1_paddle.shapesize(stretch_wid=4, stretch_len=0.5)  # Adjust the size to make it thinner and shorter
    player1_paddle.penup()
    player1_paddle.goto(-250, 0)

    # Player 2 paddle
    player2_paddle = turtle.Turtle()
    player2_paddle.shape("square")
    player2_paddle.color("white")
    player2_paddle.shapesize(stretch_wid=4, stretch_len=0.5)  # Adjust the size to make it thinner and shorter
    player2_paddle.penup()
    player2_paddle.goto(250, 0)

    # Ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=0.75, stretch_len=0.75)  # Adjust the size to make it smaller
    ball.penup()
    ball.goto(0, 0)
    # Initial ball speed (adjust as needed)
    ball_speed_x = 0.8
    ball_speed_y = 0.8
    ### Could we find a way to make it quicker as the levels pass by ?

    # Initialize scores
    score_player1 = 0
    score_player2 = 0

    # Set up the score display
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 160)
    #score_display.write("0 - 0", align="center", font=("Courier", 24, "bold"))

    # Draw dashed line
    dashed_line = turtle.Turtle()
    dashed_line.color("white")
    dashed_line.penup()
    dashed_line.hideturtle()
    ### What is this for ?

    #Set up functions for moving the paddles
    # Function to move player 1 paddle up
    def move_paddle1_up():
        y = player1_paddle.ycor()
        if y < 160:
            player1_paddle.sety(y + 25)

    # Function to move player 1 paddle down
    def move_paddle1_down():
        y = player1_paddle.ycor()
        if y > -160:
            player1_paddle.sety(y - 25)

    # Function to move player 2 paddle up
    def move_paddle2_up():
        y = player2_paddle.ycor()
        if y < 160:
            player2_paddle.sety(y + 25)

    # Function to move player 2 paddle down
    def move_paddle2_down():
        y = player2_paddle.ycor()
        if y > -160:
            player2_paddle.sety(y - 25)

    # Keyboard input for controls
    window.listen()

    # Player 1 controls
    window.onkeypress(move_paddle1_up, "w")
    window.onkeypress(move_paddle1_down, "s")

    # Player 2 controls
    window.onkeypress(move_paddle2_up, "Up")
    window.onkeypress(move_paddle2_down, "Down")

    # Set animation speed and turn on manual screen updates -> makes game quicker
    window.tracer(0)
    turtle.speed(0)

    # Main game loop
    while True:
        # Draw dashed line
        dashed_line.clear()
        dashed_line.goto(0, -200)
        dashed_line.pendown()
        dashed_line.setheading(90)
        ### I am lost about the dashed line
        
        for _ in range(20):
            dashed_line.forward(20)
            dashed_line.penup()
            dashed_line.forward(20)
            dashed_line.pendown()
        ###SOS I DON'T UNDERSTAND

        # Move the ball
        ball.setx(ball.xcor() + ball_speed_x)
        ball.sety(ball.ycor() + ball_speed_y)

        # Ball collision with upper and lower walls
        if ball.ycor() > 190 or ball.ycor() < -190:
            ball_speed_y *= -1
            ### Question: when i run the code on my computer i have to add a few lines here, or else the ball glitches with the walls, but it works well on github. Do I add my lines or are they unecessary ?

        # Ball collision with paddles
        if (
                (240 < ball.xcor() < 250)
                and (player2_paddle.ycor() + 20 > ball.ycor() > player2_paddle.ycor() - 20)
        ) or (
                (-240 > ball.xcor() > -250)
                and (player1_paddle.ycor() + 20 > ball.ycor() > player1_paddle.ycor() - 20)
        ):
            ball_speed_x *= -1

        # Check for scoring
        # Player 1 scores
        if ball.xcor() > 290:
            score_player1 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1
            ball_speed_y = random.choice([-1, 1])  # Randomize the y-direction

        # Player 2 scores
        if ball.xcor() < -290:
            score_player2 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1
            ball_speed_y = random.choice([-1, 1])  # Randomize the y-direction

        # Update the score display
        score_display.clear()
        score_display.write(f"{score_player1} - {score_player2}", align="center", font=("Courier", 24, "bold"))

        # Update the screen
        screen.update()
        ### Why ?

        # Pause briefly to control the speed of the game
        turtle.delay(10)

        # Check wether to exit the game
        if screen.getcanvas().winfo_reqheight() <= 1:  # window is closed
            break

def setup_1_player():
    import turtle

    # Set up the screen
    screen = turtle.Screen()
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=600, height=400)

    # Create paddles and ball
    player1_paddle = turtle.Turtle()
    player1_paddle.shape("square")
    player1_paddle.color("white")
    player1_paddle.shapesize(stretch_wid=3, stretch_len=0.5)  # Adjust the size to make it thinner and shorter
    player1_paddle.penup()
    player1_paddle.goto(-250, 0)

    player2_paddle = turtle.Turtle()
    player2_paddle.shape("square")
    player2_paddle.color("white")
    player2_paddle.shapesize(stretch_wid=3, stretch_len=0.5)  # Adjust the size to make it thinner and shorter
    player2_paddle.penup()
    player2_paddle.goto(250, 0)

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=0.75, stretch_len=0.75)  # Adjust the size to make it smaller
    ball.penup()
    ball.goto(0, 0)

    # Set initial ball speed (adjust as needed)
    ball_speed_x = 0.8
    ball_speed_y = 0.8

    # Initialize scores
    score_player1 = 0
    score_player2 = 0

    # Set up the font for displaying scores
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 160)

    # Draw dashed line
    dashed_line = turtle.Turtle()
    dashed_line.color("white")
    dashed_line.penup()
    dashed_line.hideturtle()

    # Set up the keyboard bindings for continuous movement
    screen.listen()

    # Function to move player 1 paddle up
    def move_paddle1_up():
        y = player1_paddle.ycor()
        if y < 160:
            player1_paddle.sety(y + 25)

    # Function to move player 1 paddle down
    def move_paddle1_down():
        y = player1_paddle.ycor()
        if y > -150:
            player1_paddle.sety(y - 25)

    # Player 1 controls
    screen.onkeypress(move_paddle1_up, "w")
    screen.onkeypress(move_paddle1_down, "s")

    # Set animation speed and turn on screen updates
    screen.tracer(0)
    turtle.speed(0)

    # Main game loop
    while True:
        # Draw dashed line
        dashed_line.clear()
        dashed_line.goto(0, -200)
        dashed_line.pendown()
        dashed_line.setheading(90)
        for _ in range(20):
            dashed_line.forward(20)
            dashed_line.penup()
            dashed_line.forward(20)
            dashed_line.pendown()

        # Move the ball
        ball.setx(ball.xcor() + ball_speed_x)
        ball.sety(ball.ycor() + ball_speed_y)

        # Move player 2 paddle towards the ball (AI)
        if player2_paddle.ycor() < ball.ycor():
            player2_paddle.sety(player2_paddle.ycor() + 1)
        elif player2_paddle.ycor() > ball.ycor():
            player2_paddle.sety(player2_paddle.ycor() - 1)

        # Ball collision with walls
        if ball.ycor() > 190 or ball.ycor() < -190:
            ball_speed_y *= -1

        # Ball collision with paddles
        if (
                (ball.xcor() > 240 and ball.xcor() < 250)
                and (ball.ycor() < player2_paddle.ycor() + 20 and ball.ycor() > player2_paddle.ycor() - 20)
        ) or (
                (ball.xcor() < -240 and ball.xcor() > -250)
                and (ball.ycor() < player1_paddle.ycor() + 20 and ball.ycor() > player1_paddle.ycor() - 20)
        ):
            ball_speed_x *= -1

        # Check for scoring
        if ball.xcor() > 290:
            # Player 1 scores
            score_player1 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1

        elif ball.xcor() < -290:
            # Player 2 scores
            score_player2 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1

        # Update the score display
        score_display.clear()
        score_display.write(f"{score_player1} - {score_player2}", align="center", font=("Courier", 24, "normal"))

        # Update the screen
        screen.update()

        # Pause briefly to control the speed of the game
        turtle.delay(10)

        # Check for a key press to exit the game
        if screen.getcanvas().winfo_reqheight() <= 1:  # window is closed
            break


# Function to handle clicks on the screen
def on_click(x, y):
    if -70 < x < 70 and -15 < y < 5:  # Click within the "Two Player" text bounding box
        # Clear landing page
        welcome_text.clear()
        mode_text.clear()
        two_player_text.clear()
        ai_text.clear()

        # Set up the game for two players
        setup_2_players()
    elif -150 < x < 140 and -55 < y < -35:  # Click within the "AI Mode" text bounding box
        # Clear landing page
        welcome_text.clear()
        mode_text.clear()
        two_player_text.clear()
        ai_text.clear()

        # Set up the game for one player
        setup_1_player()

# Bind click events to screen
screen.onscreenclick(on_click)

# Update the screen
screen.update()

# Listen for click events
turtle.mainloop()
