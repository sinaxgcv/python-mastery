# Don't do this
squares = []
for i in range(0, 10):
    squares.append(i**2)
    squares = []
    for i in range(0, 10):
        squares.append(i**2)

# But do this
squares = [i**2 for i in range(0, 10)]