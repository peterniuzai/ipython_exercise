#-*- coding: UTF-8 -*-
#组合图

import numpy as np
from matplotlib import pyplot as plt
# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)
#自定义子图区域，需要先构建一个list，由左下角坐标，宽，高组成，来生成子图[x,y,w,h]
left_x,left_y=0.1,0.1
width,height=0.65,0.65
left_xh=left_x+width+0.02
left_yh=left_y+height+0.02

scatter_area=[left_x,left_y,width,height]
hist_x=[left_x,left_yh,width,0.2]
hist_y=[left_xh,left_y,0.2,height]


plt.figure(1, figsize=(8, 8))
#生成子图的方法用到plt.axes
area_scatter=plt.axes(scatter_area)
area_histx=plt.axes(hist_x)
area_histy=plt.axes(hist_y)

#画散点图
area_scatter.scatter(x, y)

#统计散点图，画概率分布图
#设置概率分布图的bins的宽度
binwidth=0.25
#统计最大的x值，最大的y值
#np.fabs()返回绝对值
xymax=np.max([np.max(np.fabs(x)),np.max(np.fabs(y))])
#bin的数量
N_bins=int(xymax/binwidth)+1
#最大坐标
lim=N_bins*binwidth
#最小坐标
nlim=-lim
#坐标轴的分布
bins=np.arange(nlim,lim+binwidth,binwidth)
#根据取得的坐标分布，将散点图的坐标轴与此对应
area_scatter.set_xlim(nlim,lim)
area_scatter.set_ylim(nlim,lim)
#画出概率分布图
area_histx.hist(x, bins=bins)
area_histy.hist(y, bins=bins, orientation='horizontal')
#设置概率分布图的坐标
area_histx.set_xlim(area_scatter.get_xlim())
area_histy.set_ylim(area_scatter.get_ylim())
plt.show()
