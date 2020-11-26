# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 10:10 上午 

from lxml import etree
import requests

'''
https://new.qq.com/ch2/insurance
'''

tgt_filename1 = 'urls3.txt'
tgt_filename2 = 'urls3_ressult_data.tsv'


def get_content(url):
    url = url.strip()
    print(url)
    res = requests.get(url)
    _element = etree.HTML(res.text)
    texts = _element.xpath("//div[@class='content-article']/p/text()")
    content = ''
    for text in texts:
        content += text.strip()
    title = _element.xpath("//h1/text()")[0]
    return title, content


if __name__ == "__main__":

    urls = open(tgt_filename1).readlines()

    with  open(tgt_filename2, 'w') as f:
        for url in urls:
            title, content = get_content(url)
            f.write(title + '\t' + content + '\n')
