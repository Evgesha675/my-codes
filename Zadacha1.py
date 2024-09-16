c = 0
max = 0
a,b = 0,0
for x in range(0,100):
    for y in range(0,100):
        if x+y==100:
            c = x*y
            if c > max:
                max = c
                a = x
                b = y
print(max, a, b)