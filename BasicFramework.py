#Assumes (StartX, StartY, EndX, EndY) format of boxes
def calcCenter(box):
    return ((box[2]+box[0])/2, (box[3]+box[1])/2)

#Will be replaced with OCR
def parseText(box):
    return "Sample Text for Box at " + str(box)

#Assumes there is more than one box on the screen
def closestBox(box, boxes, boxCenters):
    smallestDistance = -1
    finalBox = None
    for key in boxCenters.keys():
        distanceTo = (boxCenters[key][0] ** 2 + boxCenters[key][1] ** 2) ** 0.5
        if((smallestDistance == -1 or distanceTo < smallestDistance) and key != box):
            smallestDistance = distanceTo
            finalBox = key
    return finalBox

boxes = []
boxCenters = {}
boxText = {}
labelBoxes = [] #List of the boxes themselves that contain labels
closestToLabel = {}
boxLabels = {} #Dictionary from the boxes themselves that contain labels to the label that they represent
#Box 0 Center of 2.0, 2.0
boxes.append((1.0,1.0,3.0,3.0))

#Box 1 Center of 2.0, 5.0
boxes.append((1.0, 4.0, 3.0, 6.0))

#Box 2 Center of 3.0, 2.0
boxes.append((2.0, 1.0, 4.0, 3.0))

#Populate Centers/Text for all boxes
for i in range(0, len(boxes)):
    boxCenters[boxes[i]] = calcCenter(boxes[i])
    boxText[boxes[i]] = parseText(boxes[i])
    print("Box " + str(i) + " Center: " + str(calcCenter(boxes[i])))
    print("Box " + str(i) + " Text: " + str(parseText(boxes[i])))

labelBoxes.append(boxes[0])
boxLabels[labelBoxes[0]] = "Label 1"
#Loop through all of the labelBoxes and find the closestBox to them
for i in labelBoxes:
    closestToLabel[i] = closestBox(i, boxes, boxCenters)

#Can do whatever we want with the text/box/center of the box we've found at this point to add it to our dataset
for i in labelBoxes:
    print(boxLabels[i] + ": " + boxText[closestToLabel[i]])