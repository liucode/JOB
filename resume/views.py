#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from tools.dbcon import *
from online.models import User
from resume_tool.run import *
from resume_tool.all_extractor2 import *
from resume_tool.main import *

import json
import sys 
import random 
reload(sys)  
sys.setdefaultencoding('utf8') 

import os
  
def index(req):
    if req.method == 'GET':
        try:
            islogin = req.session['islogin']
        except Exception,e:
            msg = '请登录'
            return render(req,'msg.html', locals())
        
        if req.session['islogin'] == True:
            user_info = req.session['user_info']
            condition = {'name': user_info['name']}
            r = User.objects.get(**condition)
            print r.myresume
            if r.myresume != None:
                flag = 0
                path = sys.path[0]
                result_list = process(path+"\\"+r.myresume+'.txt')
                info_list = result_list[0]
                ship_list = result_list[1]
                skill_list = result_list[2]
                project_list = result_list[3]
                socre_list = result_list[4]
                word_list = []
                for skill in skill_list:
                    word = {}
                    word['text'] = skill
                    word['weight'] = random.uniform(100, 1000)
                    word_list.append(word)
                word_list = json.dumps(word_list)
                return  render(req,"resumeindex.html", locals())
            else:
                flag = 1
                return  render(req,"resumeindex.html", locals())
        else:
            msg = '请登录'
            return render(req,'msg.html', locals())
        
def upload_file(req):  
    if req.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =req.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")  
        path = sys.path[0]
        filename = path+"\\"+myFile.name
        destination = open(filename,'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()
        result_list,myresume = runresume(myFile.name)
        name = req.session['user_info']['name']
        User.objects.filter(name=name).update(myresume=myresume)
        info_list = result_list[0]
        ship_list = result_list[1]
        skill_list = result_list[2]
        project_list = result_list[3]
        socre_list = result_list[4]
        word_list = []
        for skill in skill_list:
            word = {}
            word['text'] = skill
            word['weight'] = random.uniform(100, 1000)
            word_list.append(word)
        word_list = json.dumps(word_list)
        return  render(req,"resumeindex.html", locals()) 
