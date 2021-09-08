#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use
import time

turtle.colormode(255)
turtle.listen()
turtle.tracer(0)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)


#=======Add your code here======
time.sleep(2) # pause before drawing

# disclaimer
font = ("arial", 30,"normal")
turtle.write('this is an art piece.\nit reflects the views of Dr. Z and no one else.'+ 
             '\nyou do not have to agree with Dr. Z on this subject!',
             font=font, align="center")
time.sleep(5)
turtle.clear()
time.sleep(3)

turtle.up() # pick up pen

# draw the platter
turtle.shape("circle")
turtle.shapesize(15,35)
turtle.color("aliceblue")
turtle.goto(-15,-180)
turtle.stamp()
turtle.goto(-15,-160)
turtle.shapesize(10,25)
turtle.color("lightsteelblue")
turtle.stamp()

# change the shape back
turtle.shape("classic")
turtle.shapesize(1)

# draw turkey body
turtle.color("chocolate")
turtle.width(2)
turtle.goto(13.0, 1.0)
turtle.down()

turtle.begin_fill()
turtle.goto(39.0, 5.0)
turtle.goto(50.0, 29.0)
turtle.goto(59.0, 54.0)
turtle.goto(88.0, 34.0)
turtle.goto(114.0, -4.0)
turtle.goto(138.0, -58.0)
turtle.goto(134.0, -124.0)
turtle.goto(99.0, -179.0)
turtle.goto(49.0, -211.0)
turtle.goto(-31.0, -212.0)
turtle.goto(-141.0, -207.0)
turtle.goto(-208.0, -189.0)
turtle.goto(-245.0, -144.0)
turtle.goto(-277.0, -99.0)
turtle.goto(-307.0, -70.0)
turtle.goto(-289.0, -36.0)
turtle.goto(-249.0, -14.0)
turtle.goto(-222.0, 2.0)
turtle.goto(-162.0, 24.0)
turtle.goto(-102.0, 48.0)
turtle.goto(-82.0, 56.0)
turtle.goto(-71.0, 47.0)
turtle.goto(-66.0, 48.0)
turtle.goto(-62.0, 59.0)
turtle.goto(-48.0, 32.0)
turtle.goto(-18.0, 12.0)
turtle.goto(1.0, -1.0)
turtle.goto(19.0, 2.0)
turtle.end_fill()

# draw leg bone
turtle.up()
turtle.color('ivory')
turtle.goto(-209.0, -61.0)
turtle.down()

turtle.begin_fill()
turtle.goto(-276.0, -7.0)
turtle.goto(-295.0, -14.0)
turtle.goto(-311.0, -0.0)
turtle.goto(-306.0, 26.0)
turtle.goto(-271.0, 34.0)
turtle.goto(-258.0, 29.0)
turtle.goto(-260.0, 46.0)
turtle.goto(-239.0, 66.0)
turtle.goto(-221.0, 57.0)
turtle.goto(-214.0, 34.0)
turtle.goto(-232.0, 14.0)
turtle.goto(-170.0, -57.0)
turtle.end_fill()

# draw the leg
turtle.up()
turtle.color('saddlebrown')
turtle.goto(-170.0, -56.0)
turtle.down()
turtle.goto(-121.0, -76.0)
turtle.goto(-86.0, -104.0)
turtle.goto(-83.0, -148.0)
turtle.goto(-110.0, -171.0)
turtle.goto(-160.0, -173.0)
turtle.goto(-192.0, -140.0)
turtle.goto(-213.0, -91.0)
turtle.goto(-211.0, -64.0)

# draw the wing
turtle.up()
turtle.goto(-5.0, -36.0)
turtle.down()
turtle.goto(-11.0, -61.0)
turtle.goto(-76.0 ,-57.0)
turtle.goto(-120.0, -37.0)
turtle.goto(-129.0, -26.0)
turtle.goto(-103.0, -10.0)
turtle.goto(-61.0, -15.0)
turtle.up()
panel.update()

# skin texture
turtle.right(60)
turtle.goto(95.0, -65.0)
turtle.stamp()
turtle.goto(110.0, -115.0)
turtle.stamp()
turtle.goto(74.0, -156.0)
turtle.stamp()
turtle.goto(30.0, -131.0)
turtle.stamp()
turtle.goto(69.0, -97.0)
turtle.stamp()
turtle.goto(73.0, -30.0)
turtle.stamp()
turtle.goto(94.0, 1.0)
turtle.stamp()
turtle.goto(48.0, -185.0)
turtle.stamp()
turtle.goto(68.0, -178.0)
turtle.stamp()
panel.update()

# add text
text = "Eat the rich"
font = ("Blood of Dracula", 100, "bold")
turtle.goto(-250, 242)
turtle.color("black")
turtle.write(text, font=font)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
panel.mainloop()