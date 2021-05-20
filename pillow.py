import os, sys
from PIL import Image

# CONVERTING IMAGES INTO JPEG
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("Cannot convert", infile)






# OPENING AND SHOWING AN IMAGE
# im = Image.open('im2.png')
# im.show()
