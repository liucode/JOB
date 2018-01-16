#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from tools.dbcon import *
from online.models import User
import json
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
            return  render(req,"com_index.html", locals())
        else:
            msg = '请登录'
            return render(req,'msg.html', locals())
    if req.method == 'POST':
        msg = "模式错误"
        return  render(req,"msg.html", locals())  
            
    
def info(req):
    if req.method == 'POST':
        user_info = req.session['user_info']
        condition = {'name': user_info['name']}
        r = User.objects.get(**condition)
        if r.beans<5:
            msg = '用户豆不够，请充值'
            return render(req,'msg.html', locals())
        else:
            try:
                text=req.POST.get("comtext",'')
                my_db = MynewcoderDB()
                sqlstr =  "SELECT * from company where 标题   like '%"+text+"%'"
                infos = my_db.getInfo(sqlstr)
                infos = infos[0]
                jsname = json.dumps(infos[1])
                jsdata = []
                data = [float(infos[8])*20,float(infos[9])*20,1000,infos[1],infos[1]]
                jsdata.append(data)
                jsdata=json.dumps(jsdata)
                beans = r.beans - 5
                User.objects.filter(name=user_info['name']).update(beans=beans)
                req.session['beans'] = beans
                my_db.close()
                return  render(req,"com_index.html", locals())  
            except Exception,e:
                msg = '没有该公司，请重新查询'
                return render(req,"msg.html", locals())

