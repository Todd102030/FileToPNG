import Image, sys

im = Image.open(sys.argv[1])

width, height = im.size

#pixrgb = im.getpixel((200, 200))

decoded = ""

for y in range (0,height):
	for x in range (0,width):
		rgb = im.getpixel((x, y))
		#print rgb
		decoded += chr(rgb[0])
		#decoded += chr(rgb[1])
		#decoded += chr(rgb[2])
		#decoded.join(chr(rgb[1]))
		#decoded.join(chr(rgb[2]))
		#rgb.join(rgb)

#for l in decoded:
#	print l
#print pixrgb[2]

print decoded


