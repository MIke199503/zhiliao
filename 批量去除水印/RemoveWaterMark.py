import cv2
import numpy as np
from PIL import Image
import os

def removeWaterMark(jpgPath,newpath):
    path = jpgPath
    newPath = newpath

    img=cv2.imread(path)
    hight,width,depth=img.shape[0:3]

    #截取
    cropped = img[int(hight*0.8):hight, int(width*0.7):width]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(newPath, cropped)
    imgSY = cv2.imread(newPath,1)

    #图片二值化处理，把[200,200,200]-[250,250,250]以外的颜色变成0
    thresh = cv2.inRange(imgSY,np.array([200,200,200]),np.array([250,250,250]))
    #创建形状和尺寸的结构元素
    kernel = np.ones((3,3),np.uint8)
    #扩展待修复区域
    hi_mask = cv2.dilate(thresh,kernel,iterations=10)
    specular = cv2.inpaint(imgSY,hi_mask,5,flags=cv2.INPAINT_TELEA)
    cv2.imwrite(newPath, specular)

    #覆盖图片
    imgSY = Image.open(newPath)
    img = Image.open(path)
    img.paste(imgSY, (int(width*0.7),int(hight*0.8),width,hight))
    img.save(newPath)


if __name__ == "__main__":
    if os.path.exists("./new"):
        pass
    else:
        os.mkdir("./new")
    filespath = "./水印图片"
    os.chdir(filespath)
    filenames = os.listdir()
    print("总文件：",filenames)


    for filename in filenames:
        if filename == ".DS_Store":
            pass
        else:
            print(f"正在处理：{filename}")
            removeWaterMark(filename,"../new/"+filename)
            print(f"处理完成，文件名：{'../new/'+filename}")

