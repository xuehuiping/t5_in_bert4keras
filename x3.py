# -*- coding: utf-8 -*-
# author: huihui
# date: 2020/11/23 9:08 上午 

'''demo，查看预测结果'''

from flask import Flask, abort, request, jsonify
import random
import time

from rouge import Rouge

folder = 'result/test_data/'

# folder = 'result/valid_data/'

contents = open(folder + 'content.txt').readlines()
pred_titles = open(folder + 'pred_title.txt').readlines()
ref_titles = open(folder + 'ref_title.txt').readlines()

rouge = Rouge()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_task():
    n = random.randint(0, len(contents))
    content = contents[n].strip()
    pred_title = pred_titles[n].strip()
    ref_title = ref_titles[n].strip()

    result = {}
    result['info'] = '自动摘要-标题生成-查看预测结果'
    result['正文'] = content
    result['预测标题'] = pred_title
    result['实际标题'] = ref_title

    pred_title = ' '.join(pred_title).lower()
    ref_title = ' '.join(ref_title).lower()
    score = rouge.get_scores(hyps=pred_title, refs=ref_title)
    result['评分'] = score

    result['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return result


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=5003, debug=True)
