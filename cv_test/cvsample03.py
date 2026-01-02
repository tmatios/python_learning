
import cv2

# 画像をimgに読み込み
# img = cv2.imread("ファイル名")
img = cv2.imread("/home/bitcforex/Downloads/python/Python-3.14.2/yourvenv/source/cv_test/Tech_Teacher_blog.jpeg")

#imgの中身を表示する
#cv2.line(入力画像,左上の座標,右下の座標,BGR値,太さ)
cv2.line(img,(50, 10), (125, 600), (255, 0, 0),2)

#長方形を書く
#cv2.rectangle(入力画像,左上の座標,右下の座標,BGR値,太さ)
cv2.rectangle(img,(100,25),(300,150),(0,255,0),3)

#円を書く
#cv2.circle(入力画像,円の中心座標,半径,BGR値,太さ)
cv2.circle(img,(800,100),150,(0,0,250),-1)

#楕円を書く
#cv2.ellipse(入力画像,中心座標,長軸,短軸,楕円の傾き具合,楕円を描画する始まりの角度,終わりの角度,BGR値,太さ)
cv2.ellipse(img,(800,300),(100,50),20,0,360,(255,0,0),3)

#文字を書く
#cv2.putText(入力画像,記述する文字,文字の座標,フォント,フォントスケール,BGR値,文字の太さ,線のタイプ)
cv2.putText(img, 'OpenCV', (450, 80), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), lineType=cv2.LINE_AA)

#画像を表示する
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()