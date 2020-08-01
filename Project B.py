import  pandas as pd
# from mlxtend.frequent_patterns import apriori
from efficient_apriori import apriori
from mlxtend.frequent_patterns import association_rules
Product=pd.read_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\产品表.csv',encoding='gbk')
Orders=pd.read_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\订单表.csv',encoding='gbk')
Customer=pd.read_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\客户.csv',encoding='gbk')
Date=pd.read_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\日期表.csv',encoding='gbk')
# print(df)
print(Orders['订单日期'].dtype)
print(Date['日期'].dtype)
Sheet1=pd.merge(left=Orders,right=Date,how='left',left_on='订单日期',right_on='日期')
# print(Sheet1)

Sheet1=pd.DataFrame(Sheet1)
Sheet1.drop(['日'],axis=1,inplace=True)#这里注意输出的结果是执行此方法的结果，而不是输出test_dict_df的结果，是因为方法默认的并不是在本身执行操作，这时候输出test_dict_df输出的仍然是没有进行删除操作的原DataFrame，如果你想在原DataFrame上进行操作，需要加上inplace=True，等价于在操作完再赋值给本身：
# Sheet1.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\Sheet1.csv',encoding='gbk')
# print(Sheet1)
Sheet2=Sheet1.groupby(['客户ID']).mean()
# print(Sheet2)
# Sheet2.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project B\Sheet2.csv',encoding='gbk')
Distinct_ID=Sheet1['客户ID'].unique()
list_itemall=[]
# for i in Distinct_ID:
#     list_item=[]
#     for j in range(0,7000):
#         # print(Sheet1.iloc[0,11])
#         if Sheet1.iloc[j,11]==i:
#             list_item.append(Sheet1.iloc[j,5])
#     # print(list_item)
#     list_itemall.append(list_item)
# print(list_itemall)
for i in Distinct_ID:
    # list_item = list(set(list(Sheet1[Sheet1['客户ID']==i]['产品名称'])))#去列表重
    list_item = tuple(set(list(Sheet1[Sheet1['客户ID']==i]['产品名称'])))#去列表重

    list_itemall.append(list_item)
# print(list_itemall)
#
itemsets,aaa = apriori(list_itemall, min_support=0.02,min_confidence=0.1)
print(itemsets)
print(aaa)

# print(Sheet1[Sheet1['客户ID']==12411]['产品名称'])
# list(Sheet1[Sheet1['客户ID']==12411]['产品名称'])


    # list_item=list(Sheet1['客户ID'==i].['产品名称'])
    # print(list_item)
    # list_itemall.append(list_item)
# print(list_itemall)




