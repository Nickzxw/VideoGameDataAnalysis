#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from IPython.core.interactiveshell import InteractiveShell
from pyecharts import Bar
from pyecharts import Pie

InteractiveShell.ast_node_interactivity = "all"

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyecharts
import datetime

plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

# 警告删除
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

# 画图风格
plt.style.use("fivethirtyeight")

import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# 导入数据
df = pd.read_csv('vgdata.csv')
df.info()

# 用户喜好方向
FGE = pd.pivot_table(df, index='Year_of_Release', columns='Genre', values='Global_Sales', aggfunc=np.sum).sum().sort_values(ascending=False)
FGE = pd.DataFrame(data=FGE, columns={'Genre_sales'})
FGE_near5 = pd.pivot_table(df, index='Year_of_Release', columns='Genre', values='Global_Sales', aggfunc=np.sum).iloc[-5:, :].sum().sort_values(ascending=False)
FGE_near5 = pd.DataFrame(data=FGE_near5, columns={'Genre_sales'})
FGE_bar = Bar("用户最感兴趣的游戏类型", "长短期对比分析", title_pos='right', width=900, height=300)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
sns.barplot(x=FGE.index, y='Genre_sales', data=FGE, ax=ax1)
sns.barplot(x=FGE_near5.index, y='Genre_sales', data=FGE_near5, ax=ax2)
plt.savefig("user_interest_trend")

# 用户最喜爱的游戏平台
FPF = pd.pivot_table(df, index='Year_of_Release', columns='Platform', values='Global_Sales', aggfunc=np.sum).sum().sort_values(ascending=False)
FPF = pd.DataFrame(data=FPF, columns={'Global_Sales'})
FPF_near5 = pd.pivot_table(df, index='Year_of_Release', columns='Platform', values='Global_Sales', aggfunc=np.sum).iloc[-5:, :].sum().sort_values(ascending=False)
FPF_near5 = pd.DataFrame(data=FPF_near5, columns={'Global_Sales'})
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
sns.barplot(x=FPF.index, y='Global_Sales', data=FPF, ax=ax1)
sns.barplot(x=FPF_near5.index, y='Global_Sales', data=FPF_near5, ax=ax2)

# 企业方向
PBL = pd.pivot_table(data=df, index='Publisher', values='Global_Sales', aggfunc=np.sum)
PBL = PBL.sort_values(by='Global_Sales', ascending=False)
PBL_near5 = df[df['Year_of_Release'] > 2013]
PBL_near5 = pd.pivot_table(data=PBL_near5, index='Publisher', values='Global_Sales', aggfunc=np.sum)
PBL_near5 = PBL_near5.sort_values(by='Global_Sales', ascending=False)
pie = Pie("发行商饼状图", "长短期对比分析", title_pos='right', width=900, height=300)
pie.add("长期", PBL.head().index, PBL.head().values, center=[25, 50], is_legend_show=False, is_label_show=True)
pie.add("短期", PBL_near5.head().index, PBL_near5.head().values, center=[75, 50], is_legend_show=False, is_label_show=True)
# 保存图表
# pie.render("pie.html")

