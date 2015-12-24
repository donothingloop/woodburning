import os,sys
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Woodburning PNG2Gcode converter V0.1\n(c) 2015 donothingloop")
parser.add_argument('dotsize', metavar='-d', nargs='?', type=float, help='size of the dot in mm, best results between 0.2 and 1.0, default 0.5')
parser.add_argument('zlift', metavar='-z', nargs='?', type=float, help='amount of z-lift for moving, default 1.0')
parser.add_argument('image', help='image to convert, in PNG format')

args = parser.parse_args()
dotsize = args.dotsize

if dotsize == None:
	dotsize = 0.5

zlift = args.zlift

if zlift == None:
	zlift = 1.0

im = Image.open(sys.argv[1])
pix = im.load()

size = im.size

print(";Created by Woodburning PNG2Gcode converter V0.1")
print(";by donothingloop <donothingloop@gmail.com>")
print(";-----------------------------------------------")
print("; ")
print(";The resulting image will be %d mm by %d mm big" % (size[0]*dotsize,size[1]*dotsize))
print(";Dotsize: %f" % dotsize)
print(";Z-Lift: %f" % zlift)
print("; ")
print("G91")

def burn(strength):
	strength *= 2
	print("G1 Z-%.4f F200" % zlift)
	print("G4 P%03d" % int(strength))
	print("G1 Z%.4f F200" % zlift)

def handlePix(x,y):
	val = pix[x,y][1]

	if val > 0:
		burn(val)


for y in range(0,size[1]):
	for x in range(0,size[0]):
		handlePix(x,y)
		print("G1 X%.3f F6000" % dotsize)
	
	dist=size[0]*dotsize

	print("G1 X-%.4f F6000" % dist)	
	print("G1 Y-%.3f F6000" % dotsize)

