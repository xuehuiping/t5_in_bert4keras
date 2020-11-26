# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 3:52 下午 
import random

'''切分训练集、测试集'''

lines = open('urls2_result.tsv').readlines()
count = (int)(0.7 * len(lines))
valid_data = random.choices(lines, k=count)

with open('valid.tsv', 'w') as f:
    for e in valid_data:
        f.write(e.strip() + '\n')
