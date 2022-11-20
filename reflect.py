from __future__ import annotations
from PIL import Image, ImageStat
from typing import Tuple

from io import FileIO, TextIOBase
from tkinter import filedialog, PhotoImage, Label, Tk


class bmap(object):
    def __init__(self, img: Image.Image) -> None:
        """Crates normalized brightness matrix from image

        Args:
            img (Image.Image): input image
        """
        w = img.size[0]
        h = img.size[1]
        self.map = [[0 for x in range(h)] for y in range(w)]
        self.sum = ImageStat.Stat(img).sum[0]
        self.mapsize = (w, h)
        gray = img.convert('L')
        for i in range(w):
            for j in range(h):
                self.map[i][j] = gray.getpixel((i, j))/self.sum


class vector(object):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        """Creates xyz vector

        Args:
            x (float, optional): X value. Defaults to 0.
            y (float, optional): Y value. Defaults to 0.
            z (float, optional): Z value. Defaults to 0.
        """
        pass

    def length(self) -> float:
        """returns length of self

        Returns:
            float: length of vector self
        """
        pass

    def normalize(self) -> vector:
        """Returns normalized vector from self

        Returns:
            vector: normalized self
        """
        pass


class point(object):
    def __init__(self, x: float, y: float, z: float = 0) -> None:
        """Creates a point at x,y,z coordinates

        Args:
            x (float): X ordinate of point
            y (float): Y ordinate of point
            z (float, optional): Z ordinate of point. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.z = z
        pass

    def move(self, x: float = None, y: float = None, z: float = None) -> point:
        """Moves point by x,y,z vector

        Args:
            x (float, optional): _description_. Defaults to None.
            y (float, optional): _description_. Defaults to None.
            z (float, optional): _description_. Defaults to None.

        Returns:
            point: _description_
        """
        pass

    def __str__(self) -> str:
        return f'({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'


class mesh(object):
    def __init__(self, width: float, height: float, widthnum: int, heightnum: int) -> None:
        """Generates flat rectangular mesh of size width*height and with widthnum*heightnum vertexes

        Args:
            width (float): Physical size of mesh in X direction
            height (float): Physical size of mesh in Y direction
            widthnum (int): Number of vertexes in X direction
            heightnum (int): Number of vertexes in Y direction
        """
        self.points = [[None for x in range(heightnum)]
                       for y in range(widthnum)]
        for i in range(widthnum):
            x = -width/2+width/widthnum*i
            for j in range(heightnum):
                y = -height/2+height/heightnum*j
                self.points[i][j] = point(x, y)

    def areas(self) -> list[list[float]]:
        """Returns 2d list of polygon areas of size (widthnum-1)*(heightnum-1)

        Returns:
            list[list[float]]: 2d list of polygon areas
        """
        pass

    def normareas(self) -> list[list[float]]:
        """Returns normalized areas of polygons where sum of all areas eq 1.

        Returns:
            list[list[float]]: 2d list of normalized areas
        """
        pass

    def normals(self) -> list[list[vector]]:
        """Returns 2d list of polygon normals of size (widthnum-1)*(heightnum-1)

        Returns:
            list[list[vector]]: 2d list of polygon normals
        """
        pass

    def heights(self) -> list[list[float]]:
        """Returns 2d heightmap from self mesh of size widthnum*heightnum

        Returns:
            list[list[float]]: 2d heightmap
        """
        pass


def morphcells(imesh: mesh, brightness: bmap) -> mesh:
    """Morphes mesh cell in such a vay that cell area is proportional to pixel brightness

    Args:
        imesh (mesh): mesh of size W*H
        brightness (bmap): input brightned map of size (W-1)*(H-1)

    Returns:
        mesh: morphed mesh
    """


def rotatenormals(imesh: mesh,
                  imgsize: Tuple[float, float],
                  dist: float) -> mesh:
    """Rotate normals so that reflect from every cell falls to given image pixel

    Args:
        imesh (mesh): input mesh
        imgsize (Tuple[float, float]): physical size of image on screen 
        dist (float): distance from surface to screen 

    Returns:
        mesh: result mesh
    """
    pass


def writemesh(imash: mesh, out: TextIOBase) -> None:
    """Writes mesh to OBJ file

    Args:
        imash (mesh): input mesh
        out (str): path to obj file
    """
    pass


def genmesh(img: Image,
            dist: float,
            imgsize: Tuple[float, float],
            refsize: Tuple[float, float],
            out: TextIOBase,
            iters: int = 3) -> None:
    """Generates reflecting mesh from image

    Args:
        img (Image): input image
        dist (float): distance from reflecting surface to screen
        imgsize (Tuple[float, float]): Physical size of the image on screen located at distance dist
        refsize (Tuple[float, float]): Physical size of reflecting surface
        iters (int): number of iterations to generate final mesh
    """

    gray = bmap(img)
    refmesh = mesh(width=refsize[0],
                   height=refsize[1],
                   widthnum=gray.mapsize[0]+1,
                   heightnum=gray.mapsize[1]+1)

    for i in range(iters):
        refmesh = morphcells(refmesh, gray)
        refmesh = rotatenormals(refmesh, imgsize, dist)

    writemesh(refmesh, out)


if __name__ == '__main__':
    imgpath = 'resources/helloworld.jpg'
    img = Image.open(imgpath)
    img.show()
