# Week3 for "Stopwatch: The Game"
import simplegui
import math
# define global variables
canvas_width=200
canvas_height=200
current_time = 0
interval=100
total_count= 0
successful_count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ans = str(t/600)+":"
    if (t % 600 < 100):
        ans += str("0")
    ans += str(t%600/10)+"."+str(t%10)
    return ans
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start_handler():
    timer.start()
    
    
def Stop_handler():
    global successful_count,total_count
    if (timer.is_running() == True):
        timer.stop()
        total_count += 1
        if (current_time % 10 == 0):
            successful_count += 1
        
    
def Reset_handler():
    global current_time,total_count,successful_count
    current_time = 0
    total_count = 0
    successful_count = 0
    if (timer.is_running() == True):
        timer.stop()
        
# define event handler for timer with 0.1 sec interval
def Timer_handler():
    global current_time
    current_time += 1


# define draw handler
def draw(canvas):
    #global successful_count,
    #successful_count = 0
    canvas.draw_text(format(current_time), (50, 120), 45, 'White')
    canvas.draw_text(str(successful_count)+"/"+str(total_count), (150, 20), 30, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch", canvas_width, canvas_height) 


# register event handlers
frame.set_draw_handler(draw)
buttonStart = frame.add_button('Start', Start_handler,50)
buttonStop = frame.add_button('Stop', Stop_handler, 50)
buttonReset = frame.add_button('Reset',Reset_handler,50)

timer = simplegui.create_timer(interval, Timer_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
