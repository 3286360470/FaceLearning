from django.shortcuts import render, redirect
from PIL import Image
from FaceDetandRec import models
from .forms import RegisterForm
import datetime

import numpy as np
import cv2
import dlib
import sys

# Create your views here.
def home(request):

    pass

def uploadImg(request):
    if request.method == 'POST':
        img = models.OriPic(
            imageOri=request.FILES.get('imgOri'),
            opname=str(request.user)+str(datetime.datetime.now())+'.jpg',
            opstate=1,
            create_time=datetime.datetime.now(),
            update_time=datetime.datetime.now(),
        )
        img.save()
    return render(request, 'imgUpload.html')

def showImg(request):
    imgOri = models.OriPic.objects.get(opid='2')
    imageTar = request.FILES.get('imgTar')
    tpname = str(request.user) + str(datetime.datetime.now()) + '.jpg'
    imgTar = process(str(imgOri.imageOri), imageTar, tpname)
    # testImg = test()
    context = {
        'img':imgTar,
        # 'test': testImg
    }
    return render(request, 'showImg.html', context)

def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


def index(request):
    return render(request, 'index.html')

#
#
# def login(request):
#     pass
#

# def test():
#     img = Image.open("./zhexian.jpg")
#     return img

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

def process(imgOri, imageTar, tpname):
    image_file = './media/'+imgOri
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # t = cv2.getTickCount()
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

        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 标识出人脸区域的68个点
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    cv2.imwrite("media/imgTar/" + imgOri.split('/')[1], img=image)
    imgTar = models.TarPic(
        imageTar='imgTar/'+imgOri.split('/')[1],
        tpname=tpname,
        tpstate=1,
        create_time=datetime.datetime.now(),
        update_time=datetime.datetime.now(),
    )
    imgTar.save()
    return imgTar

git@github.com:3286360470/FaceLearning.git