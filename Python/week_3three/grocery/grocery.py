d = {}

while True:
    try:
        item = input("").upper()
    except EOFError:
        break

    if item in d:
        d[item] += 1
    else:
        d[item] = 1

for i in sorted(d.keys()):
    print(d[i], i)

