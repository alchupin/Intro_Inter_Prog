try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


def draw_circle(canvas):
    canvas.draw_circle([200, 100], 20, 3, 'red')
    
f = simplegui.create_frame('New Frame', 400, 200)
f.set_draw_handler(draw_circle)

f.start()
