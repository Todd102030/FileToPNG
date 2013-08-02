import Image, sys

textfile = open(sys.argv[1])
textstring = textfile.read()
textfile.close()

xval = 500
yval = int(len(textstring)/(xval*4) + 1)

usePass = false

#print yval

im = Image.new('RGBA', (xval,yval), (0,0,0,0))

#print xval, yval
width = xval
height = yval
count = 0

#password stuff
if sys.argv[3]:
	usePass = true

#print sys.argv[1]

for y in range (0,height):
	#count += 1
	for x in range (0,width):
		
		if usePass == true:
			
		
		if count == len(textstring) - 4:
			im.putpixel((x,y),(ord(textstring[count]),ord(textstring[count + 1]),ord(textstring[count + 2]),ord(textstring[count + 3])))
			break
		if count == len(textstring) - 3:
			im.putpixel((x,y),(ord(textstring[count]),ord(textstring[count + 1]),ord(textstring[count + 2]),0))
			break
		if count == len(textstring) - 2:
			im.putpixel((x,y),(ord(textstring[count]),ord(textstring[count + 1]),0,0))
			break
		if count == len(textstring) - 1:
			im.putpixel((x,y),(ord(textstring[count]),0,0,0))
			break
		#print "height", y, count
		#print "width", x, count
		im.putpixel((x,y),(ord(textstring[count]),ord(textstring[count + 1]),ord(textstring[count + 2]),ord(textstring[count + 3])))
		count += 4
im.save(sys.argv[2])

im.show()


#print len(textstring)

#print str(ord(val))

#print width
#print height
#print pixrgb

















