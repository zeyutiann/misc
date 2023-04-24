---
blogpost: true
date: 2023.04.25
author: TIAN Zeyu
tags: alpha-sqpt-stock
category: Interview
orphan: true
---


# Interview with WY

## Currently

HK, Quant Trading, Equity, Trading Platform (平台，提供钱，自己自负盈亏)，mid freq equity

HK 前台比较多，负责fx的大佬：qin xiayong

## SQPT

SG 是 大的research centre。

有fx future team, short term future，high freq not very profitable。

压力：还好，quant researcher不太看业绩

公司效益：最近这几年（7-8年）还不错。

去与不去最大因素：老板

junior quant researcher 主要职责：维护现有production alpha，

法国公司，做不到partner

有很多desk，每个desk不一定赚钱，但desk 赚不赚钱很重要。

面试5-6 round

team的构建：portfolio construction，signal，

parallel mobility：可以换，但不encourage，

## 他的建议

换行尽早，跳到买方要尽早。别去小公司。

## 待遇方面

130k USD base + 6-9 month bonus -> 250k USD 总包

## SQPT 面试准备：

* Regression
  * {math}`\beta = (X^TX)^{-1} X^T Y` where {math}`X^T X = Var(x)` and {math}`Cov(x,y) = X^T Y` 
  * {math}`\beta = \frac{cov(x,y)}{var(x)}=\frac{\rho * \sigma_y}{\sigma_x}`
  * {math}`t = \frac{\beta}{\sigma_{\beta}}`

* , 数据点n 增加一倍，beta 系数，t-statistics，p-value，CI怎么变
  * n：number of obs
  * p：number of variable
  * {math}`Var(\beta) = \frac{\upsilon^T \ upsilon}{n-p}`
  * {math}`t = \frac{\beta}{\sigma_{\beta}}`
  * beta wont change when n change 
* simple regression, swap x and y: {math}`y = b_1 x `, {math}`x = b_2 y`, relationship between {math}`b1, b2`. 
  * {math}`b_1 b_2 = \rho^2` 



