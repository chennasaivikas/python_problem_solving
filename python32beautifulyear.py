year = int(input()) + 1  # Start from the next year

while len(set(str(year))) != 4:
    year += 1

print(year)
