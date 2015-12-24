# woodburning.py
A PNG2Gcode converter for woodburning with a 3D printer

I use a soldering iron which is secured in place on the Z-axis bar of a K8200 3D printer.

## Result
![](http://blog.wq.lc/woodburning.jpg)
## Usage
Convert the image you want to process to black and white and resize it to the required dimensions.

```
convert image.png -colorspace Gray -resize 100x80 output.png
```

The resulting image should be 100px by 80px big. Now you can convert it.

```
python woodburning.py output.png > image.gcode
```

To print the image, simply open your favourite 3D printing software and load the GCode file.
Pay attention to disable any homing functions.

Before you start the print, disable the motors of your printer and manually move the tip of the soldering iron to the start position where you want your image to be. Then move it exactly 1mm up.

## Notes
The converter outputs the resulting size of the image as comment on top of the gcode. Make sure that the piece of wood is big enough. If it is to small, simply resize the image as this will also change the size of the resulting image.

You can also play with the *dotsize* option.

For more information enter:
```
python woodburning.py -h
```
