first = 0
nextOne = 1
for i in range(0, 10):
    print(first)
    first, nextOne = nextOne, first + nextOne