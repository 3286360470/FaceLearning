import numpy as np
import cv2
import dlib, sys

'''
人脸检测算法实现
'''
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

def resize(image, width):
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

def process(imgOri):
    image_file = './media/'+imgOri
    # resultSet = []
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("../shape_predictor_68_face_landmarks.dat")
    # predictor = dlib.shape_predictor(sys.argv[1])
    # for image_file in sys.argv[2:]:
    # t1 = cv2.getTickCount()
    image = cv2.imread(image_file)
    image = resize(image, width=1200)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)

        (x, y, w, h) = rect_to_bb(rect)
        # 绿色框框选中识别出的人脸
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 标识出人脸区域的68个点
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    image = resize(image, width=400)
    # t2 = cv2.getTickCount()
    # resultSet.append((t2-t1)/cv2.getTickFrequency())
    # cv2.imshow('img', image)
    # cv2.waitKey(0)
    # print(resultSet)
    cv2.imwrite("media/imgTar/" + imgOri.split('/')[1], img=image)
#
# if __name__ == "__main__":
#     process()

