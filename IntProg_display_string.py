try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global value

value = 3.12

# define draw handler
def draw(canvas):
    canvas.draw_text(str(value), [100, 100], 24, 'Red')

# define an input field handler
def input_handler(text):
    global value
    value = text

# create frame
frame = simplegui.create_frame('Converter', 300, 200)

# register event handler
frame.set_draw_handler(draw)
frame.add_input('Enter value', input_handler, 100)

frame.start()
