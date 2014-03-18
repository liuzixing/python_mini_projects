# Week4 game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2,HEIGHT / 2]
ball_vel = [1,2]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0 
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, 
#else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2,HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 5)
    else:
        ball_vel[0] = -random.randrange(2, 5)
    ball_vel[1] = -random.randrange(2,5)
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0 
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    #check collides with the left and right gutters
    winner = 3
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] > paddle1_pos + PAD_HEIGHT or ball_pos[1] < paddle1_pos:
            winner = RIGHT
        else:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
            
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] > paddle2_pos + PAD_HEIGHT or ball_pos[1] < paddle2_pos:
            winner = LEFT
        else:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Blue", "Yellow")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos < 0:
        paddle1_pos = 0
    if paddle1_pos + PAD_HEIGHT > HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle2_pos + PAD_HEIGHT > HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    if winner == LEFT:
        score1 += 1
        spawn_ball(LEFT)
    if winner == RIGHT:
        score2 += 1
        spawn_ball(RIGHT)
        
        
    # draw paddles
    c.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos]\
                    , [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]],\
                   1, 'Yellow', 'Orange')
    c.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos],\
                    [WIDTH, paddle2_pos + PAD_HEIGHT], \
                    [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], 1, 'Yellow', 'Orange')
    
    # draw scores
    c.draw_text(str(score1), (80, 50), 50, 'Red', 'serif')
    c.draw_text(str(score2), (WIDTH - 95, 50), 50, 'Blue', 'serif')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -10
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 10
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -10
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 10
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
          
def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler, 80)

# start frame
new_game()
frame.start()
