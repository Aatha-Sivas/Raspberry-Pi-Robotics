from pygame import *

init()

screen = display.set_mode ((640, 480))
display.set_caption("The amazing key presser!")

endProgram = False

while not endProgram:
    for e in event.get():
        if e.type == KEYDOWN:
            if (e.key == K_a):
                print("A was pressed")
            elif (e.key == K_b):
                print("B was pressed")
            elif (e.key == K_ESCAPE):
                endProgram = True
            else:
                print("ERRORZ - WRONG KEY")
                
