import cv2

#imput image
input_img=cv2.imread('images/logo.png')
cv2.imshow('Input Image',input_img)
cv2.waitKey(0)

#output image method1
output_img1=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/Output_gray_test4_method1.jpg',output_img1)
cv2.imshow('Output Image',output_img1)
cv2.waitKey(0)

#output method 2
input_img=cv2.imread('images/logo.png',0)
cv2.imshow('Output Image method2',input_img)
cv2.imwrite('images/Output_gray_test4_method2.jpg',input_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
