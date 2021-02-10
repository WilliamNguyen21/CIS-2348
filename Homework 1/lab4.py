#William Nguyen
#1824617
import math
height = int(input('Enter wall height (feet):'))
print()
width = int(input('Enter wall width (feet):'))
print()
area = height*width
paint = area/350
cans = math.ceil(paint)
print('Wall area:', area, 'square feet')
print('Paint needed:', '{:.2f}'.format(paint), 'gallons')
print('Cans needed:', cans, 'can(s)')
print()
color_dict = dict([('red', 35), ('blue', 25), ('green', 23)])
color = input('Choose a color to paint the wall:')
print()
print("Cost of purchasing", color, 'paint:', '${}'.format(color_dict[color]*cans))