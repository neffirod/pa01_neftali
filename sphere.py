# sphere.py
# Neftali Rodriguez, 04/19/17

import math
pi=math.pi


def circumference(r):
    circumference=2*pi*r
    return(circumference)

def area(r):
    area=pi*r**2
    return(area)

def surface(r):
    surface=4*pi*r**2
    return(surface)

def volume(r):
    volume= (4/3)*pi*r**3
    return(volume)



# solution must be above this comment

# do not change any part of the code below
def main():
    radius = float( input("enter radius: ") )
    print("circumference: {0:.1f}".format(circumference(radius)))
    print("circle area: {0:.1f}".format(area(radius)))
    print("sphere volume: {0:.1f}".format(volume(radius)))
    print("sphere surface area: {0:.1f}".format(surface(radius)))

main()


