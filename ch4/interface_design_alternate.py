# alternate interface design
# demonstrates interface design - focusses on parameters required for a function based on what the function does and desired output
# H@cker 03Jun2016

import math
import turtle
def polygon(t,l,n):
    for i in range(n):
        t.fw(l)
        t.tl(angle = int(360/n))
def circle(t,r):
    circimference = 2 * math.pi * r

bob = turtle.Turtle()
circle(bob,50)
