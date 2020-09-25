import cv2, time

def Capture_Gray_Image():
    '''
    Function to Capture a Image and return it in grayscale
    '''
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, img = vc.read()
    else:
        rval = False
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if not rval:
        return []
    else:
        return img

def get_Ambient_light_Value(img):
    '''
    Function to return ambient lighting value.

    It returns average of calculation through two methods.

    Method1: Compress an image to a single pixel and extract its value.

    Method2: Iterate throuch all the pixels of the image and find their average

    Returned Value: (Method1+Method2)/2
    '''
    if not img:
        return -99

    m1_val = (cv2.resize(img, (1 , 1)))[0][0]

    m2_val = 0

    r = len(img)
    c = len(img[0])
    for rows in img:
        m2_val+=(sum(rows))/c

    m2_val = m2_val/r

    return (m1_val+m2_val)/2







    
    





'''import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ans = 0
    for rows in gray:
        ans+=(sum(rows))/len(rows)

    ans = ans/len(gray)

    print(ans)

    resize_img = cv2.resize(gray  , (1 , 1))

    print(resize_img[0][0])

    print(f'Final: {(ans+resize_img[0][0])/2}')

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")


'''
'''
import cv2

vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

ans = 0
for rows in gray:
    ans+=(sum(rows))/len(rows)

ans = ans/len(gray)

print(ans)

resize_img = cv2.resize(gray  , (1 , 1))

print(resize_img[0][0])

print(f'Final: {(ans+resize_img[0][0])/2}')

cv2.imshow('img' , resize_img)
x = cv2.waitKey(20)
if x == 27:
    cv2.destroyWindow('img')

vc.release()'''
'''
echo 400 | sudo tee /sys/class/backlight/intel_backlight/brightness
'''