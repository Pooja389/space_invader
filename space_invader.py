from turtle import Turtle, Screen

screen = Screen()
screen.title("SPACE INVADER")
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic screen updates for smoother control

aliens = []

# Create aliens
for i in range(16):
    alien = Turtle()
    alien.shape("turtle")
    alien.shapesize(1.5)
    alien.color("white")
    alien.penup()
    if i < 8:
        alien.goto(-280 + i * 35, 230)
    if i >= 8:
        i = i - 8
        alien.goto(-280 + i * 35, 180)
    alien.setheading(270)
    aliens.append(alien)

# Draw initial screen with aliens placed
screen.update()

# Player setup
jet = Turtle()
jet.shape("arrow")
jet.shapesize(2)
jet.color("white")
jet.penup()
jet.goto(0, -230)
jet.setheading(90)

# Movement functions
def move_left():
    x = jet.xcor()
    if x > -280:  # Prevent moving off screen
        x -= 40
    jet.setx(x)

def move_right():
    x = jet.xcor()
    if x < 280:  # Prevent moving off screen
        x += 40
    jet.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Bullet setup
bullet_state = "ready"
bullet = Turtle()
bullet.shape("circle")
bullet.color("red")
bullet.penup()
bullet.hideturtle()  # Hide the bullet initially

# Bullet shoot function
def shoot():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(jet.xcor(), jet.ycor() + 10)
        bullet.setheading(jet.heading())
        bullet.showturtle()

# Move bullet upward
def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        bullet.forward(20)  # Increase this value to adjust bullet speed

        if bullet.ycor() > 300:  # Reset bullet if it moves out of bounds
            bullet.hideturtle()
            bullet_state = "ready"

screen.onkey(shoot, "space")

# Alien movement variable
var = 2  # Adjust for desired alien speed

# Main game loop function
def game_loop():
    global var
    move_bullet()
    for alien in aliens:
        x = alien.xcor() + var
        alien.setx(x)
        
        # Reverse direction at screen edge
        if alien.xcor() > 280 or alien.xcor() < -280:
            var *= -1
            for a in aliens:
                a.sety(a.ycor() - 20)  # Move aliens down each time they hit edge

        # Check for collision with bullet
        if bullet.distance(alien) < 20:
            alien.hideturtle()
            aliens.remove(alien)
            bullet.hideturtle()
            bullet.goto(400,-400)
            
            bullet_state = "ready"
            

      # Update bullet movement
    screen.update()  # Update screen once per loop iteration
    screen.ontimer(game_loop, 50)  # Control game loop speed

# Start the game loop
game_loop()

screen.exitonclick()
