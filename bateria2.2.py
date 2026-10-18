
GROWTH = 0.06
uso = float(input("Current usage (GB): "))

for month in range(1, 4):
    uso = uso * (1 + GROWTH)
    print(f"Month {month}: {round(uso, 2)} GB")
