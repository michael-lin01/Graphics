if __name__ == "__main__":
    f = open('image.ppm','w')
    f.write('P3 500 500 255\n')
    r = 0
    g = 0
    b = 255
    for row in range(500):
        for col in range(500):
            color = '%d %d %d ' % (r,g,b)
            f.write(color)
            g = (g+1)%256
            r = (r+1)%256
    f.close()
