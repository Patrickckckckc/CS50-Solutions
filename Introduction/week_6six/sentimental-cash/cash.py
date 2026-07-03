from cs50 import get_float

# INPUT (POSITIVE VALUES)
while True:
    money = get_float("Money: ")
    if money > 0:
        money = round(money * 100)
        break
# CALCULATE
total = 0
for i in (25, 10, 5, 1):
    total += money // i
    money %= i

print(f"{total}")
