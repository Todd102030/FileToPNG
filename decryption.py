import Image, sys
im = Image.open(sys.argv[1],'r')
width, height = im.size
decoded = ""
for y in range (0,height):
	for x in range (0,width):
		rgb = im.getpixel((x, y))
		decoded += chr(rgb[0])
		decoded += chr(rgb[1])
		decoded += chr(rgb[2])
		decoded += chr(rgb[3])
fileDecoded = open(sys.argv[2],"w")
fileDecoded.write(decoded)
fileDecoded.close()


