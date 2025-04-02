import cv2

def im_proc():
    img = cv2.imread("images/variant-2.png")
    #h, w = img.shape[:2]
    #c_x, c_y = w//2, h//2

    #M = cv2.getRotationMatrix2D((c_x, c_y), 40, 1.0)
    #rotated = cv2.warpAffine(img, M, (w, h))
    blur = cv2.GaussianBlur(img, (11,11) ,100)


    cv2.imshow("image", blur)
    



im_proc()

cv2.waitKey(0)
cv2.destroyAllWindows()
