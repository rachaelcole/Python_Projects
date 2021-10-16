print('\n******************\n')
# Chapter exercises
secs_in_week = 24 * 60 * 60 * 7
print(secs_in_week)
print('\n******************\n')

service_charge = .15
cents = 100
total_price_EUR = 24.95
final_total_EUR = int( cents * total_price_EUR * service_charge) / cents
print(final_total_EUR)

print('\n******************\n')
# Exercise 4.1
var1 = 12
var2 = 7
var3 = 23
average = (var1 + var2 + var3)/3
print(average)

print('\n******************\n')
# Exercise 4.2
pi = 3.14159
radius = 6
surface_area = radius * radius * pi
print(f'The surface area of a circle with radius {radius} is {surface_area}.')

print('\n******************\n')
# Exercise 4.3
amount_given = 1290

dollars = amount_given // 100
remainder_1 = amount_given % 100
quarters = remainder_1 // 25
remainder_2 = remainder_1 % 4

dimes = remainder_2 // 10
remainder_3 = remainder_2 % 10

nickels = remainder_3 // 5
remainder_4 = remainder_3 * 1
pennies = remainder_4

print(f'Amount given in cents: {amount_given} \n'
      f'Dollars: {dollars} \n'
      f'Quarters: {quarters} \n'
      f'Dimes: {dimes} \n'
      f'Nickels: {nickels}\n'
      f'Pennies: {pennies}\n')

print('\n******************\n')
# Exercise 4.4: swap two variables
a = 17
b = 23
print("a = ", a, " and b = ", b)
a += b  # a = 40, b = 23
b = (b - a)*-1
a -= b
print("a = ", a, " and b = ", b)
