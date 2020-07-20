from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
import random
# Create your views here.
def send_sms(request):#发送短信
    code = random.randrange(1000,9999)
    res = send_sms_single('18846826282',666366,[code,])
    print(res)
    return HttpResponse('成功')

