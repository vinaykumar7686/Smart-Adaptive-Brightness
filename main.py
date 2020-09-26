import cv2, time, os, platform 

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

    It returns average of calculation through two methods.

    Method1: Compress an image to a single pixel and extract its value.

    Method2: Iterate throuch all the pixels of the image and find their average

    Returned Value: (Method1+Method2)/2
    '''
    if not img.any():
        return -99

    m1_val = (cv2.resize(img, (1 , 1)))[0][0]

    m2_val = 0

    r = len(img)
    c = len(img[0])
    for rows in img:
        m2_val+=(sum(rows))/c

    m2_val = m2_val/r

    return (m1_val+m2_val)/2

def set_brightness(value):
    '''
    Function to set Brightness of the Screen
    '''
    value = min(50, value)

    if plt == "Windows":
        print("Applying Brightness changes to your Windows System")
        os.system(f"powershell.exe (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{2*value})")

    elif plt == "Linux":
        print("Applying Brightness changes to your Linux System")
        os.system(f"echo {min(7500,max(400,(400+(value-1)*145)))} | sudo tee /sys/class/backlight/intel_backlight/brightness")


if __name__ == "__main__":
    ans = 0
    for _ in range(3):
        ans+=(get_Ambient_light_Value(Capture_Gray_Image()))
    
    a_light = int((ans//10)+1)
    print(f"Ambient Light Detected: {a_light}")

    set_brightness(a_light)
