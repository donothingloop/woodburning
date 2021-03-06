import os,sys
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Woodburning PNG2Gcode converter V0.1\n(c) 2015 donothingloop")
parser.add_argument('--dotsize', nargs='?', type=float, help='size of the dot in mm, best results between 0.2 and 1.0, default 0.5')
parser.add_argument('--zlift', nargs='?', type=float, help='amount of z-lift for moving, default 1.0')
parser.add_argument('--zspeed', nargs='?', type=int, help='speed of the z-axis, default 200')
parser.add_argument('--factor', nargs='?', type=int, help='set it higher and the printing will get darker, usually between 150 and 250, default 200')
parser.add_argument('image', help='image to convert, in PNG format')

args = parser.parse_args()
dotsize = args.dotsize

if dotsize == None:
	dotsize = 0.5

zlift = args.zlift

if zlift == None:
	zlift = 1.0

zspeed = args.zspeed

if zspeed == None:
	zspeed = 200

factor = args.factor

if factor == None:
	factor = 200

im = Image.open(args.image)
pix = im.load()

size = im.size
duration = 0

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
        global duration
	strength *= (factor/100)
	print("G1 Z-%.4f F%03d" % (zlift,zspeed))
	print("G4 P%03d" % int(strength))
	print("G1 Z%.4f F%03d" % (zlift,zspeed))
        duration += strength

def handlePix(x,y):
	val = pix[x,y][0]

	if val > 0:
		burn(val)


for y in range(0,size[1]):
	for x in range(0,size[0]):
		handlePix(x,y)
		print("G1 X%.3f F6000" % dotsize)
	
	dist=size[0]*dotsize

	print("G1 X-%.4f F6000" % dist)	
	print("G1 Y-%.3f F6000" % dotsize)

print(";The print will take AT LEAST %d ms" % duration)
