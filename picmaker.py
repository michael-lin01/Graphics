if __name__ == "__main__":
    f = open('image.ppm','w')
    f.write('P3 500 500 500\n')

    r = 500
    for row in range(500):
        g = row
        for col in range(500):
            b = col
            color = '%d %d %d ' % (r,g,b)
            f.write(color)
    f.close()
