meters = float(input('Enter the distance in meters: '))
print('The measure of {}m corresponds to:'.format(meters))
print('{}km'.format(meters / 1000))
print('{}hm'.format(meters / 100))
print('{}dam'.format(meters / 10))
print('{:.0f}dm'.format(meters * 10))
print('{:.0f}cm'.format(meters * 100))
print('{:.0f}mm'.format(meters * 1000))
