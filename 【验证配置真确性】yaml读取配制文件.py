# -*- coding:utf-8 -*-
import yaml
import os
#验证配置文件对不对
# 作者：上海-qiweb 交流QQ：908701702

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "qiwebkeyConfig.yaml")

# open方法打开直接读出来
f = open(yamlPath, 'r')
cfg = f.read()
print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg)  # 用load方法转字典
print(d)
print u'配置文件正确'
#print(type(d))