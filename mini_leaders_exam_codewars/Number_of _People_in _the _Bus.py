def number(bus_stops):
    total = 0
    for stop in bus_stops:
        total += stop[0]
        total -= stop[1]
    return total

print(number([(10, 0), (3, 5), (5, 8)]))
print(number([(0, 0), (0, 0), (0, 0)]))
print(number([(5, 3), (10, 5), (2, 3)]))