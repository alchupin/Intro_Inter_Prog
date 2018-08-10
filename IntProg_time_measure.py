try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# global variables
first_click = True
counter = 0

# draw handler
def draw(canvas):
    canvas.draw_text(str(counter/100.0), [85, 100], 24, 'white')

# timer handler
def tick():
    global counter
    counter += 1
    

# button hadler
def click():
    global first_click, counter
    if first_click == True:
        first_click = False
        timer.start()
    else:
        first_click = True
        timer.stop()
        print(counter/100.0, ' sec')
        counter = 0
        


# create frame and timer

f = simplegui.create_frame('Counter with buttons', 200, 200)
f.add_button('Click me', click, 200)
timer = simplegui.create_timer(10, tick)
f.set_draw_handler(draw)

# start frame and timer

f.start()
