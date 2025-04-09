string = "m1i2t3h4"
total = 0

for char in string:
    if char.isdigit():
        total += int(char)

print(total)
