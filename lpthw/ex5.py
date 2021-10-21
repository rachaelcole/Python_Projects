name = 'Zed A. Shaw'
age = 35
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f'Let\'s talk about {name}.')
print(f'He\'s about {height} inches tall.')
print(f'He\'s {weight} pounds heavy.')
print(f'Actually, that\'s not too heavy.')
print(f'He\'s got {eyes} eyes and {hair} hair.')
print(f'His teeth are usually {teeth} depending on the coffee.')

total = age + height + weight
print(f'If I add {age}, {height}, and {weight}, I get {total}.')

height_cm = height * 2.54
weight_kg = weight / 2.2046

print(f'His height in cm is {height_cm:.2f}cm.')
print(f'His weight in kg is {weight_kg:.2f}kg.')
