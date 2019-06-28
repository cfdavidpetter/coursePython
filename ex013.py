salary = float(input("What is the employee's salary? $"))
increase = salary + (salary * 15 / 100)
print('The employee who wins ${:.2f} with a 15% increase goes on to receive ${:.2f}.'.format(salary, increase))