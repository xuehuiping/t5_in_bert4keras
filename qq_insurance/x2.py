# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 2:47 下午

'''爬取数据，获取网页url'''

def f1():
    content = open('保险-腾讯网.html.mhtml').read()
    content = content.replace('\n', '')
    with open('result.txt', 'w') as f:
        f.write(content)


def f2():
    content = open('result.txt').read()
    content = content.replace('https://new.qq.com/omn/', '\nhttps://new.qq.com/omn/')
    with open('result.txt', 'w') as f:
        f.write(content)


def f3():
    lines = open('result.txt').readlines()
    with open('result.txt', 'w') as f:
        for line in lines:
            line = line.strip().split('"')[0]
            f.write(line + '\n')


# f1()
# f2()
# f3()

def f4():
    lines = open('result.txt').readlines()
    urls = []
    for line in lines:
        line = line.strip()
        if line.endswith('.html') and line not in urls:
            print(line)
