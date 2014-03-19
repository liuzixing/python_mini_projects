# Week2_"Guess the number"_mini-project
# http://www.codeskulptor.org/#user20_IA90LhAGw0_4.py
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
secretNumber = 0
guessTimeleft = 0
gameRange = 100

# helper function to start and restart the game
def new_game():
    # remove this when you add your code
    global secretNumber
    secretNumber = random.randrange(0, gameRange)
    global guessTimeleft
    guessTimeleft = int(math.ceil(math.log(gameRange,2)))
    print 'New game. Range is from 0 to',gameRange
    print 'Number of remaining guesses is',guessTimeleft,'\n'
    frame.start()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global gameRange
    gameRange = 100
    # remove this when you add your code
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global gameRange
    gameRange = 1000
    # remove this when you add your code    
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print 'Guess was ', guess
    global guessTimeleft
    guessTimeleft -= 1
    print 'Number of remaining guesses is',guessTimeleft
    if int(guess) == secretNumber:
        print 'Correct!\n'
        new_game()
    elif int(guess) < secretNumber:
        print 'Higher!\n'
    else:
        print 'Lower!\n'
    if (guessTimeleft == 0) and (int(guess) != secretNumber):
        print 'you lost the game!\n'
        new_game()
    # remove this when you add your code

# create frame
frame = simplegui.create_frame('Guess the Number', 300, 300)


# register event handlers for control elements
frame.add_button('Range [0,100)',range100,200)
frame.add_button('Range [0,1000)',range1000,200)
frame.add_input('Enter a GUESS',input_guess,200)


# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
