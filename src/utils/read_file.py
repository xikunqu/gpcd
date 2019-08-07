'''
说明：读取yaml文件
'''

'''
yaml文件格式如下：
- user1:
    姓名:  张三
    电话:  13000000000
    性别:  男
- user2:
    姓名:  李四
    电话:  13000000001
    性别:  男
---
- user1:
    姓名:  王二
    电话:  13000000001
    性别:  女
'''

import yaml,os
from config.p_path import CONFIG_FILE

class YamlRead(object):
    '''读取yaml格式文件'''

    def __init__(self,filename):
        if os.path.exists(filename):
            self.yamlf=filename
        else:
            raise FileNotFoundError('文件不存在！')

    def read(self):
        with open(self.yamlf,'rb') as f:
            #yaml.load只能加载一个文档，若在一个文件中写了多个document，则使用load_all
            #yaml.safe_load_all(f)是yaml对象，此处转化为列表
            '''
            读取列表后，list[]指的是一个文档,list[][]是指item,具体根据
            所写文档的层数，自行读取，列表中存储的是字典格式
            输出如下：[[{'user1': {'电话': 13000000000, '姓名': '张三', '性别': '男'}}, {'user2': {'电话': 13000000001, '姓名': '李四', '性别': '男'}}], [{'user1': {'电话': 13000000001, '姓名': '王二', '性别': '女'}}]]
            '''

            self.data=yaml.load(f)

        return self.data