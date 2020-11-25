# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 2:59 下午 

from lxml import etree
import requests


def get_content(url):
    url = url.strip()
    print(url)
    res = requests.get(url)
    _element = etree.HTML(res.text)
    texts = _element.xpath("//div[@class='content-article']/p/text()")
    content = ''
    for text in texts:
        content += text.strip()
    titles = _element.xpath("//h1/text()")
    title = ''
    if len(titles) > 0:
        title = titles[0]
    return title, content


if __name__ == "__main__":

    urls = open('urls.txt').readlines()
    print(len(urls))
    urls = set(urls)
    print(len(urls))

    with open("qq_insurance.tsv", 'w') as f:
        for url in urls:
            title, content = get_content(url)
            f.write(title + '\t' + content + '\n')
