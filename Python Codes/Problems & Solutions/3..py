print("Enter weight on earth")
e = float(input())

print("Enter surface gravity of planet")
g = float(input())

def calc_weight_on_planet(e,g):
    p = e*(g/9.8)
    return (p)

print("Equivalent weight on the planet")
print(calc_weight_on_planet(e,g))

