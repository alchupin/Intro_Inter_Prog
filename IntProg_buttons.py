try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
# initialize globals
store = 0
operand = 0

# define event handlers

def output():
    '''prints content of store and operand'''
    print ('Store = ', store)
    print ('Operand = ', operand)
    print ('')

def swap():
    '''swap contents of store and operand'''
    global store, operand
    store, operand = operand, store
    output()

def add():
    '''add operand to store'''
    global store
    store = store + operand
    output()

def sub():
    '''subtract operand from store'''
    global store
    store = store - operand
    output()

def mult():
    ''' multiply store by operand'''
    global store
    store = store * operand
    output()

def div():
    ''' divide store by operand'''
    global store
    store = store / operand
    output()

def enter(inp):
    global operand
    operand = float(inp)
    output()


# create a frame

f = simplegui.create_frame('Calculator', 300, 300)

# register event handlers

f.add_button('Print', output, 100)
f.add_button('Swap', swap, 100)
f.add_button('Add', add, 100)
f.add_button('Sub', sub, 100)
f.add_button('Mult', mult, 100)
f.add_button('Div', div, 100)
f.add_input('Enter operand', enter, 100)

# start frame

f.start()



