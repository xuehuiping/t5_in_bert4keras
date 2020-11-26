# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/25 2:57 下午
import tqdm

folder = './result/'
w1 = open(folder + 'content.txt', 'w')
w2 = open(folder + 'pred_title.txt', 'w')
w3 = open(folder + 'ref_title.txt', 'w')

lines = open('result.txt').readlines()
for line in lines:
    line = line.strip()
    if line.startswith('实际标题：'):
        w3.write(line.replace('实际标题：', '') + '\n')
    elif line.startswith('预测标题：'):
        w2.write(line.replace('预测标题：', '') + '\n')
    elif line.startswith('输入正文：'):
        w1.write(line.replace('输入正文：', '') + '\n')
w1.close()
w2.close()
w3.close()
