import cv2

# 画像をimgに読み込み
img = cv2.imread("Tech_Teacher_blog.jpeg")

#グレースケールへの変換
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#グレースケールの画像を表示
cv2.imshow("gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()