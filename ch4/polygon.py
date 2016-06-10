import turtle
import math
bob = turtle.Turtle()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    l = 2*r/100
    polygon(t,l,100)

#def arc(t,r,angle):
    l = 2*r/100
    polygon(t,l, int(360/angle))

arc(bob,100,30)
#circle(bob,100)
#polygon(bob,20,7)
