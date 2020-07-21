from django.shortcuts import render,HttpResponse
from utils.tencent.sms import send_sms_single
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import random
# Create your views here.
def send_sms(request):#发送短信
    code = random.randrange(1000,9999)
    res = send_sms_single('18846826282',666366,[code,])
    print(res)
    return HttpResponse('成功')
from django import forms
from app01 import models
class RigisterModelForm(forms.ModelForm):
    mobil_phone = forms.CharField(label='手机号',validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机号错误'),])
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码',widget=forms.PasswordInput())
    code = forms.CharField(label='验证码',widget=forms.TextInput())
    class Meta:
        model = models.UserInfo
        fields = ['username','email','password','confirm_password','mobil_phone','code']
    def __init__(self,*args,**kwargs):#不太懂
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s'%(field.label)

def register(request):
    form =RigisterModelForm()
    return render(request,'register.html',{'form':form})



