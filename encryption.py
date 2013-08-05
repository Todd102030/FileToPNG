
import Image, sys
textfile = open(sys.argv[1],'rb')
textstring = textfile.read()
textfile.close()
xval = 500
yval = int(len(textstring)/(xval*4) + 1)
im = Image.new('RGBA', (xval,yval), (0,0,0,0))
width = xval
height = yval
count = 0
for y in range (0,height):
	for x in range (0,width):
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
		im.putpixel((x,y),(ord(textstring[count]),ord(textstring[count + 1]),ord(textstring[count + 2]),ord(textstring[count + 3])))
		count += 4
im.save(sys.argv[2])








