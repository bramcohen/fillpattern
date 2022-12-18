from PIL import Image, ImageDraw
import imageio

def drawend(window, x, y, size):
    size = size/2 - 1
    window.ellipse((int(x-size), int(y-size), int(x+size), int(y+size)), fill=(0, 0, 0), width=0)

def drawone(window, centerx, centery, boxsize, steps, stepnum, m, factor):
    delta = (1-m*2)*(boxsize/2-boxsize*stepnum/steps)
    width = 3*factor
    window.line((int(centerx-delta), int(centery-boxsize/2), int(centerx+delta), int(centery+boxsize/2)), fill=(0, 0, 0), width=width)
    drawend(window, centerx-delta, centery-boxsize/2, width)
    window.line((int(centerx-boxsize/2), int(centery+delta), int(centerx+boxsize/2), int(centery-delta)), fill=(0, 0, 0), width=width)
    drawend(window, centerx-boxsize/2, centery+delta, width)

def draweverything(window, centerx, centery, boxsize, numboxes, steps, stepnum, factor):
    for i in range(numboxes):
        for j in range(numboxes):
            drawone(window, centerx+i*boxsize, centery+j*boxsize, boxsize, steps, stepnum, (i&1)^(j&1), factor)

def makeone(boxsize, numboxes, numsteps, factor):
    boxsize *= factor
    images = []
    def ni():
        img = Image.new('RGB', (numboxes*boxsize, numboxes*boxsize), (255,255,255))
        images.append(img)
        return (img, ImageDraw.Draw(img))
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, boxsize/2, boxsize/2, boxsize, numboxes, numsteps, i, factor)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, 0, 0, boxsize, numboxes+1, numsteps, i, factor)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, boxsize/2, -boxsize/2, boxsize, numboxes+1, numsteps, i, factor)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, 0, -boxsize, boxsize, numboxes+2, numsteps, i, factor)
    images = [im.resize((numboxes*boxsize//factor, numboxes*boxsize//factor)) for im in images]
    imageio.mimsave('movie.gif', images)

makeone(50, 10, 40, 16)
