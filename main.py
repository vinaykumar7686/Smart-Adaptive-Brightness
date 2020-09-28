import cv2, time, os, platform, pyautogui, numpy as np

plt = platform.system()

if plt in ["Windows", "Linux"]:
    print(f"System identified as {plt}")

else:
    print("Unidentified System")
    exit()


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

    Method: Iterate throuch all the pixels of the image and find their average

    Return Ambient Light Value between 0 to 255
    '''
    if not img.any():
        return -99

    #m1_val = (cv2.resize(img, (1 , 1)))[0][0]

    val = 0

    r = len(img)
    c = len(img[0])
    for rows in img:
        val+=(sum(rows))/c

    val = val/r
    
    return val

def set_brightness(value):
    '''
    Function to set Brightness of the Screen
    Accepts Value 1 to 50
    '''

    if plt == "Windows":
        print("Applying Brightness changes to your Windows System")
        os.system(f"powershell.exe (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{2*value})")

    elif plt == "Linux":
        print("Applying Brightness changes to your Linux System")
        os.system(f"echo {min(7500,max(400,(400+(value-1)*145)))} | sudo tee /sys/class/backlight/intel_backlight/brightness")


def screen_snap_value():
    
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''
    # Image Preview
    cv2.namedWindow("preview")
    cv2.imshow("preview", img)
    '''
    val = get_Ambient_light_Value(img)
    ret =  int((val*49)/255)+1
    # print(val,ret)

    return 51-ret


if __name__ == "__main__":
    while True:
        time.sleep(10)
        ans = 0
        for _ in range(1):
            ans+=(get_Ambient_light_Value(Capture_Gray_Image()))
        
        a_light = int((ans//10)+1)
        print(f"Ambient Light Detected: {a_light}")

        a_light = min(50, a_light)

        ssv = screen_snap_value()

        value = (ssv+2*a_light)/3

        print((ssv, a_light, value))

        set_brightness(value)
