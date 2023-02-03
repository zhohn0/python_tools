import numpy as np
import cv2

# 修改纯白背景图为透明背景图
def white2transparent(img):
    # cv2.imshow('src', img)
    print(img.shape)

    result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    for i in range(0, img.shape[0]):  # 访问所有行
        for j in range(0, img.shape[1]):  # 访问所有列
            if img[i, j, 0] > 200 and img[i, j, 1] > 200 and img[i, j, 2] > 200:
                result[i, j, 3] = 0

    cv2.imwrite('transparent.png', result)
    print(result.shape)


if __name__ == '__main__':
    img = cv2.imread("white.png")
    white2transparent(img)
    img = cv2.imread("transparent.png",cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (128, 128))
    cv2.imwrite('transparent.png', img)
    print(img.shape)