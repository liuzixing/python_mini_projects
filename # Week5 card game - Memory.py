# Week5 card game - Memory

import simplegui
import random

state = 0
previous_card = -1
current_card = -1
turns = 0
exposed = []
card_numbers = []
image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

# helper function to initialize globals
def new_game():
    global exposed,card_numbers
    card_numbers = range(0,8) + range(0,8)
    random.shuffle(card_numbers)
    tem = []
    #for i in range(16):
    #    tem.append(random.randint(0, 2))
    for i in range(16):
        tem.append(False)
    exposed = tem
    global state, previous_card, current_card,turns
    state = 0
    turns = 0
    previous_card = -1
    current_card = -1
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    idx = pos[0] / 50
    if not exposed[idx]:
        exposed[idx] = True
        global state,previous_card,current_card,turns
        if state == 0:
            #print state,previous_card,current_card
            state = 1
            previous_card = idx
            current_card = idx
            #print "->",state,previous_card,current_card
        elif state == 1:
            #print state,previous_card,current_card
            state = 2
            previous_card = current_card
            current_card = idx
            turns += 1
            #print "->",state,previous_card,current_card
        else:
            #print state,previous_card,current_card
            state = 1
            if card_numbers[current_card] != card_numbers[previous_card]:
                exposed[current_card] = False
                exposed[previous_card] = False
            previous_card = current_card
            current_card = idx
            
            #print "->",state,previous_card,current_card
        label.set_text("Turns = " + str(turns))       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    value_x = 12
    value_y = 65
    rectangle_x = 25
    rectangle_y = 50
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(card_numbers[i]), (value_x, value_y), 50, 'Red')
        else:
            canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (rectangle_x, rectangle_y), (50, 100))
        value_x += 50
        rectangle_x += 50

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric