'''
Created on 2018-1-4

@author: corey
'''

from django.shortcuts import render
from django.template.context_processors import request

def indexView(req):
    return render(req,'baseindex.html')