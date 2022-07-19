#手势计数
import cv2
import time
import os
import FaceMeshMoudle as fmm
import PoseTracing as ptr

import handtraceing as htm
wCam, hCam = 1920, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
# cap.set(4, hCam)
folderPath = "FingerImages"
myList = os.listdir(folderPath)
if ".DS_Store" in myList:
    myList.remove(".DS_Store")

overlayList = []
for imPath in range(1,7):
    image = cv2.imread(f'{folderPath}/{imPath}.jpg')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)
# print(len(overlayList))


number_set = set()

pTime = 0
detector = htm.handDetector(detectionCon=0.75)
detectorface = fmm.FaceMeshDetector(maxFaces=2)
detectorpose = ptr.poseDetector()

tipIds = [4, 8, 12, 16, 20]
flag = True
while flag:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    detectorface.findFaceMesh(img)
    detectorpose.findPose(img)

    # print(lmList)
    if len(lmList) != 0:
        fingers = []
        # 拳头
        
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 其他数字
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

        number_set.add(totalFingers)
        if  5 in number_set and 2 in number_set and 0 in number_set:
            flag = False


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#展示母亲节的内容
cv2.destroyAllWindows()
if flag == False :
    import ccc
    ccc.ShowVideo()
    





