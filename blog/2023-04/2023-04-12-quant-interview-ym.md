---
blogpost: true
date: 2023.04.12
author: TIAN Zeyu
tags: alpha-medium-stock
category: Interview
orphan: true
---

# Interview with YML

## Trade 的 Asset class 都是什么

* 主要是美国股票，什么都trade点。 
* 美国股票是可以做short selling的

## Alpha Frequency

daily prediction


## Alpha raw data

数据每天不止一个数据点，但回测时候每天会用一个数据点。

这个数据点应该是用raw data feature extract出来的。

yml说，downsample数据，每5分钟，然后把所有五分钟的数据以某种aggregation逻辑汇总，作为daily数据。


## 大概逻辑

你觉得哪些股票会长，或相对其他股票会涨的更多，你就long这个更多的，short跌的或者更少的。

## alpha horizon

prediction of D+1 with how much to buy for D+1

execution的话，这个总量会span到一天当中，用一个algo去fill，我的理解可能是vwap，minimise market impact。

prediction 和 execution 分开做

## 语言

* C++/Python
* 系统用C++写的，所有的feature extraction module，backtesting module，每个人自己都有自己的code，甚至是regression
* 常用的ml lib会有专门的dev去搓
* 较大的ml lib会有专门的api

## 面试都考什么

* technical 不怎么面编程
* 有一定流程
* 相关经历比较重要，有些策略会比较好
* 做题 - 数学竞赛，笔试会比较差
* 招应届生比较多
* 实习会让你来的

## 年龄

应届生

太senior的人可能会down pay

## team hierarchy 是什么样

大team，research组的人做的都一样。

researcher 会给所有pm写feature，做一些数据清理，down-sample 数据，
pm 把alpha放一起做交易，自己也写alpha，看哪个alpha好。

一个pm带着几个researcher sub pm，像一个小的子公司。

quant dev：写框架，写api，不translate code，不让看 alpha code

## 有没有人带

组里的pm带，common的知识会教，简单的知识会教，避免掉坑里，策略核心的东西不会教，大家也不会问。

code 出bug了，帮忙debug。

需要数据，数据找谁要。

一来的时候，会让你用简单的idea来试一下，用系统跑一下，看下样本外performance怎么样，看下样本外是怎么样的。

实在做不出来，mentor会让你看paper，

长时间做不出来，会被开掉，策略的样本外performance一定要好的策略。

## 怎么看researcher的evaluation

三个月看一次，有没有写出新的alpha，没有live alpha 就 看样本外的表现。长时间写不出有用的alpha可能就要被开除。

你表现不好，老板会示你来加班。老板会说几次，mentor有一定帮忙。

样本外的强有一定的criteria

## 需要自己学的

一开始是让你实现一些paper，paper比如国内的研报。

technical 要求不高

数学统计一定要好

很多东西要自己推一遍，要把一些东西推成close form的形式：假设每个股票不能买超过1%，那asset allocation应该什么是最优解，有点convex optimisation的意思。

假设今天的return是明天的return，但我的constraint是risk management，怎么找最优解。用线性回归，手搓。

手搓的优势：可以改细节。

矩阵运算

日频

随机分析的东西他不用，但要是懂的话可能会有用。不会就不会往哪个方面想。 

## backtest framework

* 怎么测评：今天的预测值*明天的return，把所有的加起来
* 不太用event driven backtesting
* vectorised做到什么车程度可以上线：实盘是pm来决定。
* alpha 看五年的performance，他portfolio 的max draw down一般不能超过1%，单个alpha 的mdd不超过5%，所以不会出现margin call，因为有risk management
* alpha alpha 之间的correlation 不超过6%，但4%也有可能
* backtest 没考虑到的东西：market impact model
* 不太看rmse
* 不太看market impact
* 看的是相对的

## python 的用途

调用包，validate某个idea好不好用，用python

c++ 脚本，没有类似rolling的function，很多常用function 要自己写

关于trigger，只看D+1

feature处理 一般都是自己处理。

真正的backtest还是用的c++脚本，因为那是production code，可以rolling 来optimise 这个model 的outcome


## 实盘和非实盘

如何确保你写的code没有问题？

随机看某十天的performance，但不告诉你那10天，所以你optimisation 并不能只用那10天的数据去optimise。


## ML相关

forward testing only

不需要cross validation 去optmise

19年以后都是out of sample

## 复现paper

卖方研报，可能跟因子相关，金融工程方向，什么名字没太听清。。中金国际？

数学模型：比如deep learning相关，时间序列比较准的paper，预测天气什么的。

time series arima 的各种变体，用在不同的factor上，

## 如何确定一个feature对预测 investment有用。
arima 用在财报上，这个data 以及这个data的feature上，然后需要确定下这个arima预测的值和asset value的值是否是highly correlated相关。

## 如何看某个数据是否有利用价值

首先这个数据的frequency是什么样子的

这个数据和股票价值的相关性，绝对值越大越好。

该数据维数够多，直接扔到deep learning的数据里面去，让它去train。

## 建议

先找一家练一练手，看看什么样子。带prediction比较相关。

## 注意：

以下信息不要和他同公司人聊。