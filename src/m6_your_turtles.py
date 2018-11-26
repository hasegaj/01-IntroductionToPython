"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Josiah Hasegawa.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

nope = rg.SimpleTurtle('turtle')
nope.pen = rg.Pen('blue', 2)
nope.speed = 15

size = 125

for k in range(3):
    nope.draw_square(size)

    nope.pen_up()
    nope.backward(20)

    nope.pen_down()
    size = size - 15

yup = rg.SimpleTurtle('turtle')
yup.pen = rg.Pen('green', 3)
yup.speed = 14

sizew = 100

for k in range(4):
    yup.draw_circle(sizew)

    yup.pen_up()
    yup.forward(12)
    yup.left(12)

    yup.pen_down()
    sizew = sizew - 13

window.close_on_mouse_click()