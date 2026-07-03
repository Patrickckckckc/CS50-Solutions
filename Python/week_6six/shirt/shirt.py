import sys
from PIL import Image, ImageOps

# Check CLA
if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")

infile = sys.argv[1]
outfile = sys.argv[2]

# Split name and extension safely
try:
    inName, inExtension = infile.rsplit(".", 1)
    outName, outExtension = outfile.rsplit(".", 1)
except ValueError:
    sys.exit("Invalid file name format")

# Allowed extensions
extensionType = ["jpg", "jpeg", "png"]

# Validate extensions
if inExtension.lower() not in extensionType or outExtension.lower() not in extensionType:
    sys.exit("Invalid output")

# Check matching extensions
if inExtension.lower() != outExtension.lower():
    sys.exit("Input and Output have different extensions")

# Try opening files
try:
    muppetPhoto = Image.open(infile)
    shirtPic = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")

# Resize muppet to shirt size
shirtSize = shirtPic.size
muppet = ImageOps.fit(muppetPhoto, shirtSize)

# Paste shirt on top (respect transparency)
muppet.paste(shirtPic, (0, 0), shirtPic)

# Save final image
muppet.save(outfile)
