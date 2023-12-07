import turtle
import random

w_pressed = False
s_pressed = False


def setup_1_player():
    """
    Set up a single-player Pong game with keyboard controls for the player.

    This function initializes the game screen, paddles, ball, scores, and keyboard bindings.
    The player controls their paddle using the 'w' and 's' keys to move up and down, respectively.
    The AI controls the second paddle to follow the y-coordinate of the ball to make the game challenging.

    Controls:
    - 'w': Move the player's paddle up
    - 's': Move the player's paddle down

    The game loop continuously updates the ball, paddles, and scores while checking for collisions.
    The game window closes when the user exits.
    """

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
    ball_speed_x = 1
    ball_speed_y = 1

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
    def stop_move_paddle1_up():
        global w_pressed
        w_pressed = False

    def stop_move_paddle1_down():
        global s_pressed
        s_pressed = False

    def move_paddle1_up():
        if player1_paddle.ycor() < 160:
            player1_paddle.sety(player1_paddle.ycor() + 2)

    def move_paddle1_down():
        if player1_paddle.ycor() > -150:
            player1_paddle.sety(player1_paddle.ycor() - 2)

    # Player 1 controls
    screen.onkeypress(move_paddle1_up, "w")
    screen.onkeypress(move_paddle1_down, "s")

    # Set animation speed and turn on screen updates

    def press_w():
        global w_pressed
        w_pressed = True

    def press_s():
        global s_pressed
        s_pressed = True

    turtle.listen()
    turtle.onkeypress(press_w, "w")
    turtle.onkeyrelease(stop_move_paddle1_up, "w")
    turtle.onkeypress(press_s, "s")
    turtle.onkeyrelease(stop_move_paddle1_down, "s")

    screen.tracer(0)
    turtle.speed(0)

    # Main game loop
    while True:
        if w_pressed:
            move_paddle1_up()
        if s_pressed:
            move_paddle1_down()

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
            if player2_paddle.ycor() < 160:
                player2_paddle.sety(player2_paddle.ycor() + 1)
        elif player2_paddle.ycor() > ball.ycor():
            if player2_paddle.ycor() > -150:
                player2_paddle.sety(player2_paddle.ycor() - 1)

        # Ball collision with walls
        if ball.ycor() > 190 or ball.ycor() < -190:
            ball_speed_y *= -1

        # Ball collision with paddles
        if (
                (240 < ball.xcor() < 250)
                and (player2_paddle.ycor() + 35 > ball.ycor() > player2_paddle.ycor() - 35)
        ):
            ball.setx(240)
            ball_speed_x *= -1

        if (
                (-240 > ball.xcor() > -250)
                and (player1_paddle.ycor() + 35 > ball.ycor() > player1_paddle.ycor() - 35)
        ):
            ball.setx(-240)
            ball_speed_x *= -1

        # Check for scoring
        if ball.xcor() > 290:
            # Player 1 scores
            score_player1 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1
            ball_speed_y = random.uniform(-1, 1)  # Randomize the y-direction

        elif ball.xcor() < -290:
            # Player 2 scores
            score_player2 += 1
            ball.goto(0, 0)
            ball_speed_x *= -1
            ball_speed_y = random.uniform(-1, 1)  # Randomize the y-direction

        # Update the score display
        score_display.clear()
        score_display.write(f"{score_player1} - {score_player2}", align="center", font=("Courier", 24, "normal"))

        # Update the screen
        screen.update()
