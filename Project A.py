from bs4 import BeautifulSoup
import requests
import pandas as pd
from html.parser import HTMLParser

dia = {}
list_max=[]
list_min=[]
list_type=[]
list_url=[]
for url in ['http://car.bitauto.com/xuanchegongju/?g=2&c=4&mid=8','http://car.bitauto.com/xuanchegongju/?g=2&c=4&mid=8&page=2','http://car.bitauto.com/xuanchegongju/?mid=8&page=3']:
    print(url)
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    html=requests.get(url,headers=headers,timeout=10)
    text=html.text
    # print(i)
    soup=BeautifulSoup(text,'html.parser')
    # print(soup)

    # print(temp)
    Type=soup.find_all(class_='cx-name text-hover')
    # print(Type[0].text)

    Price=soup.find_all(class_='cx-price')
    temp = soup.find_all('div', class_='search-result-list-item')
    for k in range(len(temp)):

        Href=temp[k].find('a')
    # print(Href.get('href'))
    # print((len(Type)))
        href=Href.get('href')
        Pic_url='http://car.bitauto.com%s'%href
        list_url.append(Pic_url)
    for j in range(len(Type)):
        list_type.append(Type[j].text)
    for i in range(len(Price)):
        P=Price[i].text
        min=P[0:P.rfind('-')]
        max=P[P.rfind('-')+1:-1]
        list_min.append(min)
        list_max.append(max)
print(list_type)
print(list_max)
print(list_url)

dia={'车型':list_type,'最低价格':list_min,'最高价格':list_max,'图片链接':list_url}
df=pd.DataFrame(dia,index=None)
print(df)
df.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\考试\Project A\Project A.csv',encoding='utf-8_sig')



    # q=Price[0].text
    # qq=q[0:q.rfind('-')]
    # print(qq)
    # print(Price[0].text)


    # dia = {}
    # for i in range(len(Type)):
    #
    #     dia[Type[i].text]=Price[i].text
    # # print(dia)
    # df1=pd.DataFrame(dia,index=['zhangfei'])
    # print(df1)


    # for n in temp2:
    #     name=n.find_all('cx-name text-hover')
    #     print(name.text)



#     temp=soup.find('div', class_='tslb_b')
#     # print(temp)
#     temp2=temp.find_all('tr')
#     # dia={}
#     # df=pd.DataFrame()
#     for tr in temp2:
#         td_list=tr.find_all('td')
#         # print(td_list)
#         if len(td_list)>0:
#             # print(td_list[0].text)
#          a,s,d,f,g,h,j,k=td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
#          dia['a'],dia['s'],dia['d'],dia['f'],dia['g'],dia['h'],dia['j'],dia['k']=a,s,d,f,g,h,j,k
#          # print(dia)
#          df=df.append(dia,ignore_index=True)
#          # print('a=',a)
# print(df)
# # df.to_csv(r'C:\Users\JiangBin\Desktop\统计学\VW课程\第二课\作业.csv',encoding='utf-8_sig')
#
# # print(dia)
#
# # print(soup.p
# # rettify())
# # print(soup.tr.text)
# # print(soup.find_all('tr'))
# # colume=[]
# # for c in soup.tr.text:
# #     colume.append(i)
# # print(colume)
#
# # print(i)
# # soup=BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# # soup.prettify(encoding='utf-8')
# # import requests
# # from bs4 import BeautifulSoup
# # # 请求URL
# # url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'
# # # 得到页面的内容
# # headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# # html=requests.get(url,headers=headers,timeout=10)
# # content = html.text
# '''
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36