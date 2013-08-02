import Image, sys, os

im = Image.open(sys.argv[1])

width, height = im.size

#pixrgb = im.getpixel((200, 200))
#binary_stdout = os.fdopen( sys.stdout.fileno(), 'wb' )
decoded = ""

for y in range (0,height):
	for x in range (0,width):
		rgb = im.getpixel((x, y))
		#print rgb
		#binary_stdout.write(chr(rgb[0]))
		#binary_stdout.write(chr(rgb[1]))
		#binary_stdout.write(chr(rgb[2]))
		#binary_stdout.write(chr(rgb[3]))
	#if rgb[0] != 219:
		decoded += chr(rgb[0])
	#if rgb[1] != 219:
		decoded += chr(rgb[1])
	#if rgb[2] != 219:
		decoded += chr(rgb[2])
	#if rgb[3] != 219:
		decoded += chr(rgb[3])
		##decoded.join(chr(rgb[1]))
		##decoded.join(chr(rgb[2]))
		##rgb.join(rgb)

#for l in decoded:
#	print l
#print pixrgb[2]

#sys.stdout.write(decoded)
#print(decoded)
#binary_stdout.write(decoded)
#decoded = decoed.encode(

#sys.stdout.buffer.write(b'decoded')

#sys.stdout = os.fdopen(1, "wb")
#binout = os.fdopen(sys.stdout.fileno(), "wb")
#binout.write(decoded)


fileDecoded = open(sys.argv[2],"wb")
fileDecoded.write(decoded)
fileDecoded.close()


#binary_stdout(decoded)
#print sys.stdout.mode
