numbers = [1, 2, 3, 2, 4, 2, 5, 4, 3, 1, 2]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Frequency of numbers:")
for key, value in frequency.items():
    print(f"{key} -> {value}")