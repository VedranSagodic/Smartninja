from function import pozdrav, calculate_sum, cube, pedometer, absolute, square_cube


poruka = pozdrav(name="Vedran")

print(poruka)

result = calculate_sum(1,2)

print(result)

result = calculate_sum(3242, 6543)

print(result)

result = calculate_sum(342, 653)

print(result)

print(cube(65))

print(cube(2))

result = pedometer(1500, 0.5)
print(result)

print(absolute(x=6, y=4))

square_two, cube_two = square_cube(5)
print(square_two)
print(cube_two)