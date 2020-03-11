MAX_ITER = 80

def mandelbrot(c):
    z = 0
    interations = 0
    while abs(z) <= 2 and interations < MAX_ITER:
        z = z*z + c
        interations += 1
    return interations

if __name__ == "__main__":
    for a in range(-10, 10, 5):
        for b in range (-10, 10, 5):
            c = complex(a / 10, b /10)
            print(c, mandelbrot(c))