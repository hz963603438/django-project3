# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models
from django.shortcuts import render
import os
from django.http import HttpResponse

# Register your models here.

admin.AdminSite.site_header = 'M版运维平台'
admin.AdminSite.site_title = 'M版运维平台'

#admin.site.register(models.User)



email = {0: '123456@163.com', 1: 'abcdef@qq.com', 3: '1a2b3c@11.com'}


def changeemail(modeladmin, request, queryset):
    queryset.update(email=email[0])

changeemail.short_description = 'change email'

class Userinfo(admin.ModelAdmin):
    list_display = ('name', 'email', 'sex')
    search_fields = ('name', 'sex')
    list_filter = ('name', 'email')
    actions = [changeemail]


admin.site.register(models.User, Userinfo)



#admin.site.register(models.Node)
@admin.register(models.Node)
class Show_node(admin.ModelAdmin):
    list_display = ('id', 'nodename')

    actions = ['edit_node']

    def edit_node(self, requests, queryset):
        #return render(requests, 'podlist.html')

        #os.system得到的是命令执行的返回值
        #result = os.system("kubectl get pod -owide | grep ip-172-17-53-37.cn-northwest-1.compute.internal | awk '{print $1}'").readlines()

        #将得到的结果直接赋值给列表
        #result = os.popen("kubectl get pod -owide | grep ip-172-17-53-37.cn-northwest-1.compute.internal | awk '{print $1}'")
        #return HttpResponse("all pods is %s" % result.read())

        print("queryset type is: ", type(queryset))
        print("queryset data is: ", queryset)

        for nodename in queryset:
            print("nodename is: ", nodename, "nodename type is: ", type(nodename))
            result = os.popen("kubectl get pod -owide | grep %s | awk '{print $1}'" % (nodename))
            print("result node is: ", result, "result type is: ", type(result))
            allpod = result.readlines()
            print("allpod的类型是: ", type(allpod))
            return render(requests, 'podlist.html', locals())

        #return HttpResponse("all pod is %s" % allpod)


    edit_node.short_description = '查看node'
    #edit_node.icon = 'fas fa-audio-description'
    edit_node.type = 'danger'
    edit_node.style = 'color:black;'


    # def nodedetail(self):
    #     print("node上面运行的pod")
    #
    # nodedetail.short_description = 'node详情'
    # nodedetailtype = 'success'
    # nodedetail.enable = True
    # actions = [models.Node]
    #list_display = ('nodename')
    #list_per_page = 20
