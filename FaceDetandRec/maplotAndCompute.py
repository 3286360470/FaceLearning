import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 必须配置中文字体，否则会显示成方块
# 注意所有希望图表显示的中文必须为unicode格式
# custom_font = mpl.font_manager.FontProperties(fname='../static/fonts/iconfont.ttf')

font_size = 10  # 字体大小
fig_size = (8, 6)  # 图表大小

names = (u'hog', u'cnn')  # 姓名
subjects = (u'p1', u'p2', u'p3', u'p4', u'p5', u'p6', u'p7', u'p8', u'p9', u'p10', u'p11', u'p12')  # 科目
scores = ((0.1839, 0.0858, 0.1053, 0.0817, 0.1020, 0.1149,
           0.1150, 0.1198, 0.1022, 0.1132, 0.0955, 0.1229),
          (29.4271, 8.6099, 13.2160, 9.8359, 15.7326, 14.8278,
           15.1869, 15.0167, 15.0489, 12.7522, 11.7826, 15.4404))

# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
mpl.rcParams['figure.figsize'] = fig_size
# 设置柱形图宽度
bar_width = 0.10

index = np.arange(len(scores[0]))
# 绘制「小明」的成绩
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
# 绘制「小红」的成绩
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
# X轴标题
plt.xticks(index + bar_width, subjects) #, fontproperties=custom_font
# Y轴范围
plt.ylim(ymax=30, ymin=0)
plt.xlabel("picture")
plt.ylabel("time/s")
# 图表标题
plt.title(u'Performance')#, fontproperties=custom_font
# 图例显示在图表下方
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5) #, prop=custom_font


# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        # 柱形图边缘用白色填充，纯粹为了美观
        rect.set_edgecolor('white')


add_labels(rects1)
add_labels(rects2)

# 图表输出到本地
plt.savefig('zhexian.png')
plt.show()

