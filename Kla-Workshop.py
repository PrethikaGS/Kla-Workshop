from PIL import Image, ImageChops
import cv2
import numpy as np
# Loading images

def addToFile(num,im):
    px = im.load()
    l=[]
    print(px[9,0])

    for y in range(600):
        for x in range(800):
            if px[x,y]!=(0,0,0):
                #print(px[x,y],end=" ")
                l.append([num,x,(599-y)])
    print(len(l))
    # open file in write mode
    with open('level1.csv', 'a') as file:
        for item in l:
                file.write(",".join(map(str,item)))
                file.write("\n")


def createAnomalyImg(p1,p2,p3,num):
    img1 = Image.open("D:/PSG/kla/Level_1_Input_Data/"+p1)
    img2 = Image.open("D:/PSG/kla/Level_1_Input_Data/"+p2)
    img3 = Image.open("D:/PSG/kla/Level_1_Input_Data/"+p3)

    # finding difference
    diff1 = ImageChops.difference(img1, img2) #e1+e2
    diff2 = ImageChops.difference(img1, img3) #e1+e3
    diff3 = ImageChops.difference(img2, img3) #e2+e3
    # saving the result
    diff1.save(p1+p2+".jpg")
    diff2.save(p1+p3+".jpg")
    diff3.save(p2+p3+".jpg")

    res1=Image.open("D:/PSG/kla/Level_1_Input_Data/"+p1+p2+".jpg")
    res2=Image.open("D:/PSG/kla/Level_1_Input_Data/"+p1+p3+".jpg")
    res1=res1.convert("1")
    res2=res2.convert("1")
    im3 = ImageChops.logical_and(res1, res2) 

    re1= np.array(Image.open("D:/PSG/kla/Level_1_Input_Data/"+p1+p2+".jpg"))
    re2= np.array(Image.open("D:/PSG/kla/Level_1_Input_Data/"+p1+p3+".jpg"))

    bitAnd=cv2.bitwise_and(re1, re2, mask = None)
    cv2.imwrite("an"+str(num)+".jpg", bitAnd)
    #cv2.imshow("AND", bitAnd)
    #cv2.waitKey(0)

    """resDiff1 = ImageChops.difference(res1, res2) #e1+e2+e3
    resDiff1.save("combined"+p1+p2+p3+"Error.jpg")
    res3= Image.open("D:/PSG/kla/Level_1_Input_Data/combined"+p1+p2+p3+"Error.jpg")
    res4=Image.open("D:/PSG/kla/Level_1_Input_Data/"+p2+p3+".jpg")
    finalDiff=ImageChops.difference(res3, res4) #e1
    finalDiff.save("anomaly"+str(num)+".jpg")"""
    im3.save("anomaly"+str(num)+".jpg")
    im=Image.open("D:/PSG/kla/Level_1_Input_Data/an"+str(num)+".jpg")
    addToFile(num,im)
#Die1
createAnomalyImg("wafer_image_1.png","wafer_image_3.png","wafer_image_2.png",1)
#Die2
createAnomalyImg("wafer_image_2.png","wafer_image_1.png","wafer_image_3.png",2)
#Die3
createAnomalyImg("wafer_image_3.png","wafer_image_4.png","wafer_image_2.png",3)
#Die4
createAnomalyImg("wafer_image_4.png","wafer_image_5.png","wafer_image_3.png",4)
#Die5
createAnomalyImg("wafer_image_5.png","wafer_image_1.png","wafer_image_4.png",5)
