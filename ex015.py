days = int(input("How many rented days? "))
miles = float(input("How many miles? "))

print('Total payable is ${:.2f}.'.format((60 * days) + (0.15 * miles)))
