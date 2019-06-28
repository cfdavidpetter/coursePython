from math import hypot

oppositeLeg = float(input("Length of the opposite leg: "))
adjacentLeg = float(input("Length of the adjacent leg: "))

print('The hypotenuse is {:.2f}.'.format(hypot(oppositeLeg, adjacentLeg)))
