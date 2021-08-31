import cv2
img=cv2.imread("./original.jpg",0)  #0:for ordinary
                                    #1:for RGB
                                    #-1:for alpha channel
print(img)
cv2.imshow("first img",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("second img.jpg",img)
    cv2.destroyAllWindows()
