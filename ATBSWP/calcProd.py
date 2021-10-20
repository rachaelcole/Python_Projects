import time

def calcProd():
    # Calculate product of first 100,000 numbers
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()
prod = calcProd()
end_time = time.time()

print(f'The result is {len(str(prod))} digits long.')
print(f'Took {end_time - start_time} seconds to calculate.')
