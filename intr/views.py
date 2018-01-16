#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from tools.dbcon import *
from online.models import User
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   
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
            user_info['job'] = r.job
            user_info['edu'] = r.edu
            user_info['comp'] = r.comp
            if cmp(r.comp,"")!=0 or cmp(r.edu,"")!=0 or cmp(r.job,"")!=0:
                flag = 0
                return  render(req,"intr_index.html", locals())
            else:
                flag = 1
                return  render(req,"intr_index.html", locals())
        else:
            msg = '请登录'
            return render(req,'msg.html', locals())
            
    
def info(req):
    if req.method == 'POST':
        comp = req.POST['comp']
        job = req.POST['job']
        edu = req.POST['edu']
        user_info = req.session['user_info']
        condition = {'name': user_info['name']}
        r = User.objects.get(**condition)
        beans = r.beans
        beans +=10
        User.objects.filter(name=user_info['name']).update(beans=beans,job=job,comp=comp,edu=edu)
        return  render(req,"intr_index.html", locals())     

