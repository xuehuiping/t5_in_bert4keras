# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 11:10 上午 

'''try'''
from textrank4zh import TextRank4Keyword, TextRank4Sentence

tr4s = TextRank4Sentence()


def extract_summary(filename='qq_insurance/qq_insurance.tsv'):
    w = open('qq_insurance/qq_insurance_extract.tsv', 'w')
    with open(filename, encoding='utf-8') as f:
        for l in f:
            title, content = l.strip().split('\t')
            tr4s.analyze(text=content, lower=True, source='all_filters')
            summary = ''
            for item in tr4s.get_key_sentences(num=3):
                summary += item.sentence
            w.write(title.strip() + '\t' + summary.strip()+'\n')


extract_summary()
