countEven = 0
countOdd = 0
for i in range(1, 21):
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(f"Even numbers: {countEven}")
print(f"Odd numbers: {countOdd}")