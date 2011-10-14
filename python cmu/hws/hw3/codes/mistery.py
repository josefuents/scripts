def bb(f):
    g = 1
    b = 1
    while (g < f):
        if (abs(g*g-f) < abs(b*b-f)):
            b = g
        g += 0.001
    return b
