from sklearn.cluster import KMeans as K
import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale
import matplotlib.pyplot as plt
Date=pd.read_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\CarPrice_Assignment.csv')
Date1=pd.DataFrame(Date)
# print(Date1)
# print(Date1[0:1])
# print(Date1['carbody'].unique())
# print(Date1['carbody'].dtype)
cols=Date1.columns  #分类变量变为数值型变量
for col in cols[3:]:
    if Date1[col].dtype=='object':
        L=len(Date1[col].unique())
        list_col=Date1[col].unique()
        # print(list_col)
        list_num=[]
        for i in range(1,L+1):
            # print(i)
            list_num.append(i)
        dia=dict(zip(list_col,list_num))
        # print(dia)
        # print(Date1[col])
        Date1[col]=Date1[col].map(dia)
# print(Date1)
# Date1.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\Date1.csv')
cols=list(cols)#创建新的可供聚类分析的表
del cols[0]
del cols[1]
# print(cols)
Data2=Date1[cols]
# Data2.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\Data2.csv')
Data2_std=minmax_scale(Data2)
# print(Data2_std)
inertia=[]  #画出手肘图，选取聚类簇数
for n in range(1,15):
    Train=K(n_clusters=n)
    Train.fit(Data2_std)
    inertia.append(Train.inertia_)
x=list(range(1,15))
y=inertia
plt.plot(x,y)
# plt.show()
Train=K(n_clusters=4)
Train.fit(Data2_std)
result=Train.predict(Data2_std)
# print(result)
result=pd.DataFrame(result,columns=['聚类结果'])
Data_result=pd.concat((Date1,result),axis=1)
# Data_result.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\Data_result.csv',encoding='gbk')
Categories=Data_result.groupby(['聚类结果','CarName']).mean()
print(Categories)
Categories.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\Categories.csv',encoding='gbk')
# Data_result.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project C\Data_result.csv',encoding='gbk')

# list=Date1['carbody'].unique()

# dia={}
# list2=[1,2,3,4,5]
# dia=dict(zip(list,list2))
# print(dia)
# # print(list(1,3))
# list3=[range(1,3)]
# print(list3)
