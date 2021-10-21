def count(num, increment):
    i = 0
    numbers = []
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + increment
        print(f"Numbers now: {numbers}")
        print(f"At the bottom i is {i}")


print("The numbers:")

print(count(10, 2))
