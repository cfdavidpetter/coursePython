wide = float(input('How wide is the wall?'))
tall = float(input('How tall is the wall?'))

print('Its wall has a dimension of {}x{} and its area is {}m².'.format(wide, tall, wide*tall))
print('To paint this wall, you need {}l of ink.'.format((wide*tall)*0.5))