# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 9:01 上午 

import random

'''查看预测结果'''

folder = 'result/test_data/'

folder = 'result/valid_data/'

contents = open(folder + 'content.txt').readlines()
pred_titles = open(folder + 'pred_title.txt').readlines()
ref_titles = open(folder + 'ref_title.txt').readlines()

print(len(contents) == len(ref_titles))
print(len(pred_titles) == len(ref_titles))

n = random.randint(0, len(contents))
content = contents[n]
pred_title = pred_titles[n]
ref_title = ref_titles[n]

print('正文：\n' + content + '\n')
print('预测标题：\n' + pred_title + '\n')
print('实际标题：\n' + ref_title + '\n')
