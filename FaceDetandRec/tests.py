from django.test import TestCase

# Create your tests here.
import numpy as np
import cv2
import dlib
import sys
#基于Python的人脸检测


def rect_to_bb(rect):
    '''
    对已经检测到的脸部区域进行数据加工
    :param rect: rect为dlib脸部区域检测的输出，
    :return: 返回脸部区域的边界信息左上与右下
    '''
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
    '''
    对已经检测到的脸部的脸部特征的输出的数据进行加工
    :param shape: 为dlib检测到的脸部特征值(能够描述脸部特征的68个点的坐标)
    :param dtype:
    :return: 返回了一个能够描述脸部特征的68个点的坐标的特征矩阵
    '''
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords

def resize(image, width=1200):
    '''
    调整带检测的图片的大小
    :param image: 读入的图片
    :param width:
    :return: 返回已调整过大小的图片
    '''
    r = width*1.0/image.shape[1]
    dim = (width, int(image.shape[0]*r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized


'''
通过执行脚本时传入的参数(即图片的路径)
通过执行dlib库中的detector和predictor分别来获取人脸区域检测的结果和人脸特征检测的结果数据

'''
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <image file>"%sys.argv[0])
        sys.exit(1)
    image_file = sys.argv[1]
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("/Users/dfss/Desktop/shape_predictor_68_face_landmarks.dat")

    # t = cv2.getTickCount()
    image = cv2.imread(image_file)
    image = resize(image, width=1200)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)

        (x, y ,w, h) = rect_to_bb(rect)
        #绿色框框选中识别出的人脸
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(image, "Face #{}".format(i+1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        #标识出人脸区域的68个点
        for(x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    # t = (cv2.getTickCount() - t) / cv2.getTickFrequency()
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    # print(t)
