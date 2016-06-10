# Alternate Square
# code as per book(tp2)
# H@cker 03June2016

#demonstrating Generalization

import turtle

def polygon(t,l,n):
    angle = 360 / n
    for i in range(n):
        t.fd(l)
        t.lt(angle)

sides = int(input("How many sides do you want?"))
shape = str(sides) + " sided shape"
length = int(input("how long:"))
bob = turtle.Turtle()
polygon(bob,length,sides)
print("I am done, here is your", shape)
