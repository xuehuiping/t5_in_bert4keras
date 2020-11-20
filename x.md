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
