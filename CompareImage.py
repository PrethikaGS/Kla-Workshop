from PIL import Image, ImageChops
# Loading images
img1 = Image.open("D:/PSG\kla/Level_1_Input_Data/wafer_image_1.png")
img2 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_2.png")
img3 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_3.png")
img4 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_4.png")
img5 = Image.open("D:/PSG/kla/Level_1_Input_Data/wafer_image_5.png")
# finding difference from the first die to all the remaining dies 
diff1 = ImageChops.difference(img1, img2)
diff2 = ImageChops.difference(img1, img3)
diff3 = ImageChops.difference(img1, img4)
diff4 = ImageChops.difference(img1, img5)
# saving the result to check which are the anomalies
diff1.save("result1.jpg")
diff2.save("result2.jpg")
diff3.save("result3.jpg")
diff4.save("result4.jpg")