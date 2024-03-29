#!/usr/bin/python3
import cv2

def resizeFrame(frame, scale=0.7):
    print(frame.shape)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_NEAREST)


if __name__ == '__main__':
    img = cv2.imread("../../images/draw.png")
    cv2.imshow("Image", resizeFrame(img, 3))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
