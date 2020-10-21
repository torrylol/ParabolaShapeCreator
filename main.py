
import turtle
import math
import colorsys
import random
import os

def shape(t, size):
    for tmp in range(0, int((sides))):
        t.forward(size)
        t.right(360/int(sides))


print('ParabolaShapeCreator!')
print('Create parabolas (with shapes and colours (Turtle Graphics))...')
print('')
print('Please press enter to proceed to the main menu...')
input('')
os.system('clear')

print('Shape Configuration:')
print('Please select a shape below:')
print('')
print('1. Square')
print('2. Triangle')
print('3. Octagon')
print('4. Pentagon')
print('5. Hexagon')
print('6. Heptagon')
print('7. Nonagon')
print('8. Decagon')
print('9. Pentecontagon')
print('10. Hectagon')
print('')
print('')
print('r. Random')
print('c. Custom')
print('')
shape_config = input(':')
os.system('clear')

if shape_config == '1': # Square
    sides = 4
if shape_config == '2': # Triangle
    sides = 3
if shape_config == '3': # Octogon
    sides = 8
if shape_config == '4': # Pentagon
    sides = 5
if shape_config == '5': # Hexagon
    sides = 6
if shape_config == '6': # Heptagon
    sides = 7
if shape_config == '7': # Nonagon
    sides = 9
if shape_config == '8': # Decagon
    sides = 10
if shape_config == '9': # Pentecontagon
    sides = 50
if shape_config == '10': # Hectagon
    sides = 100
if shape_config == 'c': # Custom
    print('Enter amount of sides for new shape...')
    sides = input(':')
if shape_config == 'r': # RANDOM
    sides = random.randint(1,8)

print('Colour Configuration')
print('H, S, V, Enter as a number from 1-100 (for custom)')
print('')
print('1. B&W (black and white) [BUG: CAN INCLUDE RED]')
print('2. Solid Black')
print('3. Solid White')
print('4. Red')
print('5. Green')
print('6. Blue')
print('7. RGB')
print('8. Clown Mode [NEW] [HIGHLY RATED]')
print('9. Red to light')
print('10. Random!')
print('')
print('c. Custom')
colour_select = input(':')
os.system('clear')

h_colour = 0
s_colour = 0
v_colour = 0

if colour_select == '1': # Black and White
    h_colour = random.choice([0, 100])
    s_colour = random.choice([0, 100])
    v_colour = random.choice([0, 100])
    if (h_colour == '100' and s_colour == '100' and v_colour == '100'):
        h_colour = 100
        s_colour = 000
        v_colour = 100
    phi = 180 * (3 - math.sqrt(5))
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)

    num = 200
    while True:
        for x in (range(-num, num)):
            h = int(h_colour) / 100
            s = int(s_colour) / 100
            v = int(v_colour) / 100
            t.fillcolor(colorsys.hsv_to_rgb(h, s, v))
            t.begin_fill()
            shape(t, 100 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)
            h_colour = random.choice([0, 100])
            s_colour = random.choice([0, 100])
            v_colour = random.choice([0, 100])
            if (h_colour == '100' and s_colour == '100' and v_colour == '100'):
                h_colour = 100
                s_colour = 000
                v_colour = 100
    turtle.mainloop()


if colour_select == '2': # Solid Black
    h_colour = 000
    s_colour = 100
    v_colour = 000
if colour_select == '3': # Solid White
    h_colour = 100
    s_colour = 000
    v_colour = 100
if colour_select == '4': # Red
    h_colour = 000
    s_colour = 100
    v_colour = 100
if colour_select == '5': # Green
    h_colour = 30
    s_colour = 100
    v_colour = 100
if colour_select == '6': # Blue
    h_colour = 50
    s_colour = 50
    v_colour = 100
if colour_select == '7': # RGB
    h_colour = random.choice([100, 50, 30]) /100
    s_colour = random.choice([100,100, 50]) /100
    v_colour = 1
    phi = 180 * (3 - math.sqrt(5))
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)

    num = 200
    while True:
        for x in (range(-num, num)):
            t.fillcolor(colorsys.hsv_to_rgb(h_colour, s_colour, v_colour))
            t.begin_fill()
            shape(t, 100 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)
            h_colour = random.choice([100, 50, 30]) / 100
            s_colour = random.choice([100, 100, 50]) / 100
    turtle.mainloop()

if colour_select == '8': # Clown Mode
    phi = 180 * (3 - math.sqrt(5))
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)

    num = 200
    while True:
        for x in (range(-num, num)):
            t.fillcolor(colorsys.hsv_to_rgb(x*x/num, 1, 1))
            t.begin_fill()
            shape(t, 100 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)
    turtle.mainloop()

if colour_select == '9': # Red to light
    phi = 180 * (3 - math.sqrt(5))
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)
    num = 200
    while True:
        for x in reversed(range(0, num)):
            t.fillcolor(colorsys.hsv_to_rgb(x / num, 1.0, 1.0))
            t.begin_fill()
            shape(t, 5 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)
        turtle.mainloop()
if colour_select == '10': # Random
    h_colour = random.randint(0, 100)
    s_colour = random.randint(0, 100)
    v_colour = random.randint(0, 100)
    phi = 180 * (3 - math.sqrt(5))
    t = turtle.Pen()
    t.hideturtle()
    t.speed(0)

    num = 200
    while True:
        for x in (range(-num, num)):
            h = int(h_colour) / 100
            s = int(s_colour) / 100
            v = int(v_colour) / 100
            t.fillcolor(colorsys.hsv_to_rgb(h, s, v))
            t.begin_fill()
            shape(t, 100 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)
            h_colour = random.randint(0, 100)
            s_colour = random.randint(0, 100)
            v_colour = random.randint(0, 100)
            if shape_config == 'r':
                sides = random.randint(1, 8)
            break
    turtle.mainloop()


if colour_select == 'c':
    print('Input HSV values (0-100)')
    h_colour = input('H : ')
    s_colour = input('S : ')
    v_colour = input('V : ')

phi = 180 * (3 - math.sqrt(5))
t = turtle.Pen()
t.hideturtle()
t.speed(0)

num = 200
while True:
    for x in (range(-num, num)):
        h = int(h_colour) / 100
        s = int(s_colour) / 100
        v = int(v_colour) / 100
        t.fillcolor(colorsys.hsv_to_rgb(h, s, v))
        t.begin_fill()
        shape(t, 100 + x)
        t.end_fill()
        t.right(phi)
        t.right(.8)
        if shape_config == 'r':
            sides = random.randint(1, 8)
        break
turtle.mainloop()






