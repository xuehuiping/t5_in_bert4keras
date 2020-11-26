# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 9:13 上午

'''try，计算rouge'''

from rouge import Rouge

rouge = Rouge()

pred_title = '海南省旅游交通气象服务系统模型设计与实现'
title = '通用性的专业气象产品服务系统的设计与应用'
pred_title = ' '.join(pred_title).lower()
title = ' '.join(title).lower()

r = rouge.get_scores(hyps=pred_title, refs=title)
print(r)
