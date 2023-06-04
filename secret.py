import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import time
import numpy as np

img_sphere = Image.open("images/xiaogou.jpeg")

st.subheader('翁大人，下面是今天我为你精心挑选的小狗：')
st.image(img_sphere,width=350)
#获取当天日期
cols = ['日期','使用个数','包装批次','规格','剩余个数','备注']
data = pd.DataFrame(columns=['日期','使用个数','包装批次','规格','剩余个数','备注'],\
                    data=np.array((['2023-6-3',2,'`001','10',3,'稍微有点匆忙'])).reshape(1,-1))
hdata = pd.read_excel('a.xlsx')
st.dataframe(hdata[cols])

# hdata.to_excel('a.xlsx')
#data.to_excel('a.xlsx')
now = datetime.datetime.now().strftime('%Y-%m-%d')
lastday = hdata['日期']
l = hdata['日期'].max()
st.write(l)
days = (datetime.datetime.strptime(now,'%Y-%m-%d')-datetime.datetime.strptime(l,'%Y-%m-%d')).days
st.write('尊敬的主人您好，今天是'+now+'据我所知你们上次嘿嘿的日子是'+l+'距离上次已经有'+str(days)+'天啦')
st.write('请输入本次数据')
col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    c1 = st.selectbox('使用个数',(1,2,3,4,5))
with col2:
    c2 = st.selectbox('包装批次',('`001','`002','`003','`004'))
with col3:
    c3 = st.selectbox('规格',(1,3,5,10,15,20))
with col4:
    c4 = st.selectbox('剩余个数',(1,2,3,4,5,6,7,8,9,10))
with col5:
    c5 = st.text_input('备注')
new = pd.DataFrame(columns=cols,data=np.array([now,c1,c2,c3,c4,c5]).reshape(1,-1))
#st.dataframe(new)
#st.write('请确认，没有问题就提交吧，本次表现棒棒下次继续保持哦！')
ra = st.radio('请选择是否提交',['输入状态','提交'])

if ra == '提交':
    datas = hdata.append(new)
    datas.to_excel('a.xlsx')
    st.subheader('不错不错 本次表现棒棒下次继续保持哦:sunglasses:')
    st.write('现在完整记录如下:')
    st.dataframe(datas[cols])
if st.button('删除最后一行记录'):
    datas = pd.read_excel('a.xlsx')
    if len(datas) > 1:
        datas[:-1].to_excel('a.xlsx')
        st.write('下面是更新后的结果')
        st.dataframe(datas[cols])
    else:
        st.warning('不能再删了')