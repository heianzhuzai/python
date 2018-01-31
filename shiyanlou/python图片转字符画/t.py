import Image

img = Image.open("test.png")
print img.format, img.size, img.mode

height = img.size[0]
width = img.size[1]

print height
print width

def test(r,g,b,alpha = 256):
	return r,g,b,alpha
	
txt = ""

for i in range(0, width/2):
	for j in range(0, height/2):
		txt += str(test(*img.getpixel((i,j))))
		txt += '\n'
with open("t.txt", 'w') as f:
	f.write(txt)
