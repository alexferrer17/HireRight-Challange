import pyautogui
# Take a screenshot directly to disk
# pass a four-integer tuple of the left, top, width, and height of the region to capture
def TakeScreenShot(left, top, width, height):
    pyautogui.screenshot("bounding_box.png", region=(left,top,width,height))
    return
#main
left = 0
top = 0
width = 300
height = 300
TakeScreenShot(left,top,width,height)
