import cv2
import pickle

rectW , rectH = 107 , 48



try:
    with open('carParkPos.mp4' , 'rb') as f:
        poslist = pickle.load(f)
except:
    poslist = []

def mouseClick(events, x,y,flags,paramas):
     if events == cv2.EVENT_LBUTTONDOWN:
         poslist.append((x,y))
     if events == cv2.EVENT_RBUTTONDOWN:
         for i,pos in enumerate(poslist):
             x1,y1 = pos
             if x1 < x < x1+rectW and y1 < y < y1 + rectH:
                 poslist.pop(i)
     with open('carParkPos' , 'wb' ) as f:
          pickle.dump(poslist,f)




while True:
    img = cv2.imread("img.png" )
    for pos in poslist: cv2.rectangle(img,pos,(pos[0] + rectW , pos[1] + rectH), (0,0,255) , 2)
    cv2.imshow("Image" , img)
    cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)
