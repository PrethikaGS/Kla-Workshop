from PIL import Image, ImageChops
# Loading images

img1 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_1.png")
img2 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_2.png")
img3 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_3.png")
img4 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_4.png")
img5 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_5.png")
# finding difference
diff1 = ImageChops.difference(img1, img2)
diff2 = ImageChops.difference(img1, img3)
diff3 = ImageChops.difference(img1, img4)
diff4 = ImageChops.difference(img1, img5)
# saving the result
diff1.save("result1.jpg")
diff2.save("result2.jpg")
diff3.save("result3.jpg")
diff4.save("result4.jpg")

res1=Image.open("D:/PSG/kla/Level_1_Input_Data/result1.jpg")
res2=Image.open("D:/PSG/kla/Level_1_Input_Data/result2.jpg")
resDiff1 = ImageChops.difference(res1, res2)
resDiff1.save("anomalyIn1.jpg")

im = Image.open("D:/PSG/kla/Level_1_Input_Data/anomalyIn1.jpg")
px = im.load()
#print (px[9,0])


for y in range(600):
    for x in range(800):
        if px[x,y]!=(0,0,0):
            print(1,x,y)
            