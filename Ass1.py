rows = 5
print("Lower Triangular Pattern:")
for i in range(1, rows + 1):
    print("* " * i)

print("\nUpper Triangular Pattern:")
for i in range(rows, 0, -1):
    print("* " * i)

print("\nPyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
