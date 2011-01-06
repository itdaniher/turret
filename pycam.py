import ImageFilter
import Image
import numpy
from time import sleep
from opencv import highgui, adaptors

camera = highgui.cvCreateCameraCapture(0)

def gaussian_grid(size = 5):
	"""
	Create a square grid of integers of gaussian shape
	e.g. gaussian_grid() returns
	array([[ 1,  4,  7,  4,  1],
	       [ 4, 20, 33, 20,  4],
	       [ 7, 33, 55, 33,  7],
	       [ 4, 20, 33, 20,  4],
	       [ 1,  4,  7,  4,  1]])
	"""
	m = size/2
	n = m+1  # remember python is 'upto' n in the range below
	x, y = numpy.mgrid[-m:n,-m:n]
	# multiply by a factor to get 1 in the corner of the grid
	# ie for a 5x5 grid   fac*exp(-0.5*(2**2 + 2**2)) = 1
	fac = numpy.exp(m**2)
	g = fac*numpy.exp(-0.5*(x**2 + y**2))
	return g.round().astype(int)

class GAUSSIAN(ImageFilter.BuiltinFilter):
	name = "Gaussian"
	gg = gaussian_grid().flatten().tolist()
	filterargs = (5,5), sum(gg), 0, tuple(gg)

def getImg():
	ImgOCV = highgui.cvQueryFrame(camera)
	ImgPIL = adaptors.Ipl2PIL(ImgOCV) 
	ImgPIL = ImgPIL.filter(GAUSSIAN)
	ImgRAW = ImgPIL.convert("L").tostring()
	ImgArray = numpy.frombuffer(ImgRAW, dtype=numpy.uint8)
	ImgArray = ImgArray.reshape(ImgPIL.size)
	return ImgArray

def getMovement():
	a = 0
	b = 0
	print "3"
	sleep(.25)
	print "2"
	sleep(.25)
	print "1"
	sleep(.25)
	print "cheese!"
	a = getImg()
	print "3"
	sleep(.25)
	print "2"
	sleep(.25)
	print "1"
	sleep(.25)
	print "cheese!"
	b = getImg()
	print "3"
	sleep(.25)
	print "2"
	sleep(.25)
	print "1"
	sleep(.25)
	print "cheese!"
	c = getImg()
	return a, b, c

def negToZero(x):
	return (x ^ (x >> 7) ) - (x >> 7) + x

def show(x):
	Image.frombuffer("L",(640,480),x.tostring(),'raw', "L", 0, 1).show()

def cleanup(camera):
	highgui.cvReleaseCapture(camera)
