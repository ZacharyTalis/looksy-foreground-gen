#!/usr/bin/env python3

import sys
from PIL import Image

# If help requested, print help message
if ((len(sys.argv) == 1) or ("help" in sys.argv[1])):
    helpMessage = \
"""Format: python3 main.py <x,y> <icons> <placements>

Example: To generate a 2x4 foreground image with row order \"blanks -> stars -> hearts -> blanks\"
python3 main.py 2,4 star,heart 0,0-1,1-2,2

Paths: All icons should be PNGs and reside within the \"icons\" folder. Each output is saved to the \"output\" folder as \"foreground.png\"."""
    print(helpMessage)
    sys.exit(0)

# Calculate image size (height or width) based on panel dimension
def calcImageSize(dimension):
    return (82 * dimension + 104)

# Constants (same every time)
iconDir = "icons/"
outputDir = "output/"
cellSizePx = 58 # height and width of a cell
edgeSizePx = 64 # offset from edge of image to first row/column
gapSizePx  = 82 # cellSizePx + 24px between cells

# Constants (based on arguments)
try:
    rawDimensions = [int(x) for x in sys.argv[1].split(",")]
    dimensions    = [calcImageSize(x) for x in rawDimensions]
    iconNames     = sys.argv[2].split(",")
    placements    = [x.split(",") for x in sys.argv[3].split("-")]
except:
    sys.exit("Arguments missing or not recognized! Refer to \"main.py --help\" for argument format.")

# Check if dimensions are valid, else return error
if (rawDimensions[0] <= 0):
    sys.exit(f"x dimension ({rawDimensions[0]}) must be 1 or greater!")
if (rawDimensions[1] <= 0):
    sys.exit(f"y dimension ({rawDimensions[1]}) must be 1 or greater!")

# Check if placements if valid, else return error
if (len(placements) > rawDimensions[1]):
    sys.exit("Too many rows specified!")
i = 1
failedRows = []
for row in placements:
    if (len(row) > rawDimensions[0]):
        failedRows.append(i)
    i += 1
if (len(failedRows) > 0):
    if (len(failedRows) == 1):
        sys.exit(f"Row {failedRows[0]} is longer than x dimension specified ({rawDimensions[0]})!")
    else:
        sys.exit(f"Rows {failedRows} are longer than x dimension specified ({rawDimensions[0]})!")

# Generate icon dictionary
icons = {}
for iconName in iconNames:
    try:
        icons[iconName] = Image.open(f"{iconDir}{iconName}.png")
    except:
        sys.exit(f"{iconName}.png not found in icons folder!")
    try:
        icons[iconName] = icons[iconName].resize((cellSizePx, cellSizePx))
    except:
        sys.exit("Image resize failed!")

# Generate image
baseImage = Image.new("RGBA", dimensions)
iconPlaced = False
currentY = edgeSizePx
for row in placements:
    currentX = edgeSizePx
    for iconValue in row:
        if (iconValue.isdigit()):
            iconValue = int(iconValue)
            if (iconValue > len(iconNames)):
                sys.exit(f"Specified icon value \"{iconValue}\" doesn't correspond to any specified icon!")
            if (iconValue > 0):
                baseImage.paste(icons[iconNames[iconValue - 1]], (currentX, currentY))
                iconPlaced = True
        elif (not len(iconValue) == 0):
            sys.exit(f"Icon value {iconValue} isn't a digit!")
        currentX += gapSizePx
    currentY += gapSizePx
if (not iconPlaced):
    sys.exit("No icons placements specified!")
baseImage.save(f"{outputDir}foreground.png", "PNG")
