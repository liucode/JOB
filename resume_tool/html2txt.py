# -*- coding:utf8 -*-

import sys
import logging

import re
import chardet
import html2text

import sys #这里只是一个对sys的引用，只能reload才能进行重新加载
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr 
reload(sys) #通过import引用进来时,setdefaultencoding函数在被系统调用后被删除了，所以必须reload一次
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde 
sys.setdefaultencoding('utf-8')


# 将word文档转换为txt格式
def handle_htmlfiles(htmlfile):
    fin = open(htmlfile, 'r')
    strfile = fin.read()
    #print chardet.detect(strfile)
    str_file=""
    # 文本格式的编码方式统一为utf-8
    if (chardet.detect(strfile)['encoding'] == 'GB2312'):
        str_file = html2text.html2text(strfile.decode("gbk", 'ignore').encode("utf-8", 'ignore'))
    elif ((chardet.detect(strfile)['encoding'] == 'utf-8') or (
                chardet.detect(strfile)['encoding'] == 'UTF-8-SIG')or (
                chardet.detect(strfile)['encoding'] == None)):
        str_file = html2text.html2text(strfile)
    else:
        str_file = ""
        #print str_file
    return str_file
