r = 0
for i in range(7):
    if i % 3 == 0:
        r = r + 1
    elif i % 2 == 0:
        r  = r + 2
    else:
        r = r + i
print(r)