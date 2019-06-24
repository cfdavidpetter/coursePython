num = int(input('Enter the number to see your table: '))

print('-' * 10)
for x in range(1, 11):
    print('{} x {} = {}'.format(num , x, num * x))
print('-' * 10)