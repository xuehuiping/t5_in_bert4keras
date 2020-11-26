T5中文版，mT5，实现中文的自动标题生成/文本摘要


git clone https://github.com/bojone/t5_in_bert4keras.git

39.102.115.187

xuehp@haomeiya007:~$ source ~/anaconda3/bin/activate 

source ~/anaconda3/bin/activate 

conda create --name  t5_in_bert4keras python=3.6
source ~/anaconda3/bin/activate 
conda activate t5_in_bert4keras

pip install tensorflow==1.14

(t5_in_bert4keras) xuehp@haomeiya007:~$ pip install tensorflow==1.14

pip install keras==2.3.1

pip install bert4keras==0.9.1

007机器
scp -r csl_summary_dataset xuehp@39.102.115.187:~/git/t5_in_bert4keras/
scp -r mt5 xuehp@39.102.115.187:~/git/t5_in_bert4keras/


2020年11月18日17:00:33  训练完毕，40个epoch

每个epoch需要35分钟。总共需要24小时。


数据集、预训练模型、模型文件（权重）、日志（40个epoch）均在：
链接: https://pan.baidu.com/s/19GKtsAmnZgnQGlFD27v19A  密码: oep8

在007机器训练，1块V100

在本地进行测试，加载模型并预测。

测试集测试：
{'rouge-1': 0.9427881329041697, 'rouge-2': 0.9244111176179525, 'rouge-l': 0.9402983103816833, 'bleu': 0.9045120527737623}


2020-11-23 10:07:33

以腾讯保险为例，测试中文自动摘要的效果。https://new.qq.com/ch2/insurance

https://new.qq.com/omn/20201122/20201122A0DMM000.html
https://new.qq.com/omn/20201121/20201121A0DRUY00.html
https://new.qq.com/omn/20201122/20201122A09DT500.html
https://new.qq.com/omn/20201120/20201120A0I7BT00.html
https://new.qq.com/omn/20201122/20201122A0AJTY00.html
https://new.qq.com/omn/20201122/20201122A0A7AS00.html
https://new.qq.com/omn/20201122/20201122A08LS500.html
https://new.qq.com/omn/20201123/20201123A02K0H00.html
https://new.qq.com/omn/20201123/20201123A0339Q00.html
https://new.qq.com/omn/20201120/20201120A07UQ900.html


qq_insurance2结果：
valid_data: {'rouge-1': 0.32459164257098105, 'rouge-2': 0.22526106593480874, 'rouge-l': 0.3707993023281894, 'bleu': 0.14115163467201844, 'best_bleu': 0.14115163467201844}