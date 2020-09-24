import cv2

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


'''import cv2

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
