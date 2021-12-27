from PIL import Image, ImageDraw
import imageio

def drawone(window, centerx, centery, boxsize, steps, stepnum, m):
    delta = (1-m*2)*(boxsize/2-boxsize*stepnum/steps)
    window.line((int(centerx-delta), int(centery-boxsize/2), int(centerx+delta), int(centery+boxsize/2)), fill=(0, 0, 0), width=3)
    window.line((int(centerx-boxsize/2), int(centery+delta), int(centerx+boxsize/2), int(centery-delta)), fill=(0, 0, 0), width=3)

def draweverything(window, centerx, centery, boxsize, numboxes, steps, stepnum):
    for i in range(numboxes):
        for j in range(numboxes):
            drawone(window, centerx+i*boxsize, centery+j*boxsize, boxsize, steps, stepnum, (i&1)^(j&1))

def makeone(boxsize, numboxes, numsteps):
    images = []
    def ni():
        img = Image.new('RGB', (numboxes*boxsize, numboxes*boxsize), (255,255,255))
        images.append(img)
        return (img, ImageDraw.Draw(img))
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, boxsize/2, boxsize/2, boxsize, numboxes, numsteps, i)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, 0, 0, boxsize, numboxes+1, numsteps, i)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, boxsize/2, -boxsize/2, boxsize, numboxes+1, numsteps, i)
    for i in range(numsteps):
        img, w = ni()
        draweverything(w, 0, -boxsize, boxsize, numboxes+2, numsteps, i)
    imageio.mimsave('movie.mp4', images)

makeone(50, 10, 40)
