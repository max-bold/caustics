from PIL import Image, ImageStat
from reflect import bmap, mesh


def imageopen():
    path = 'resources/helloworld.jpg'
    img = Image.open(path)
    img.show()


def imgtogray():
    path = 'resources/helloworld color.jpg'
    gray = Image.open(path).convert('L')
    gray.show()


def imgtobmap():
    path = 'resources/helloworld.jpg'
    img = Image.open(path)
    bm = bmap(img)
    newimg = Image.new(mode='L', size=bm.mapsize)
    for i in range(bm.mapsize[0]):
        for j in range(bm.mapsize[1]):
            newimg.putpixel((i, j), int(bm.map[i][j]*bm.sum))
    newimg.show()


def createmesh():
    path = 'resources/helloworld.jpg'
    img = Image.open(path)
    gray = bmap(img)
    refmesh = mesh(width=5.0,
                   height=1.0,
                   widthnum=gray.mapsize[0]+1,
                   heightnum=gray.mapsize[1]+1)
    for j in range(gray.mapsize[1]+1):
        l = ''
        for i in range(gray.mapsize[0]+1):
            l+=' '+str(refmesh.points[i][j])
        print(l)


if __name__ == '__main__':
    # imageopen()
    # imgtogray()
    # imgtobmap()
    createmesh()
