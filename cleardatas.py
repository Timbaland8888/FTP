#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Arthur:Timbaland
# Date:2018-03
import sys,time,os
import subprocess
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
import os,shutil,datetime

def mk_dir(dir):
    isexsit = os.path.exists(dir)
    if isexsit :
        print("目录%s已经存在" %(dir))
    else:
        os.mkdir(dir)
        print("目录%s" % (dir))
def acl_dir(classroom,classid):
    #切换工作目录D
    os.chdir(r'D:\临时share')
    #添加对应目录的权限
    cre_acl = 'cacls %s /e /t /g %s:R' %(classroom,classid)
    os.popen(cre_acl)
    #取消对应目录的权限
    del_acl_domain = 'cacls %s /e /t /c /r "Domain Users"' %(classroom)
    del_acl_teacher = 'cacls %s /e /t /c /r teacher' % (classroom)
    del_acl_student = 'cacls %s /e /t /c /r student' % (classroom)
    os.popen(del_acl_domain)
    os.popen(del_acl_teacher)
    os.popen(del_acl_student)
    #共享对应目录
    share_dir = 'net share %s=%s' %(classroom,base_dir + '\\' + classroom)
    print (share_dir)
    os.popen(share_dir)
# mk_dir('D:\临时share\\1403教室')
# acl_dir('1403教室','A01教室')
dit_list = {'1403教室':'A01教室','1404教室':'D01教室',
            '1405教室':'B01教室','1406教室':'E01教室',
            '1407教室': 'C01教室',}
# print(dit_list['1403教室'])
base_dir = r'D:\临时share'
if  __name__ == "__main__":
    while True:
        print("当前时间：%s" %(datetime.datetime.now().strftime('%H:%M')))
        if  datetime.datetime.now().strftime('%H:%M') in ['01:16']:

            try:
                # os.chdir(base_dir)
                #清空教室的文件
                for classroom in dit_list.keys():
                    # shutil.rmtree(classroom)
                    # print(base_dir+'\\'+classroom )
                    mk_dir(base_dir+'\\'+classroom)
                    shutil.rmtree(base_dir+'\\'+classroom)
                    mk_dir(base_dir + '\\' + classroom)
                    acl_dir(classroom,dit_list[classroom])
            # shutil.move(f,dir_teacher[0]+f)
            except Exception as e:
                # print unicode(now_date+str(f),'utf-8')
                # print os.rename(f,f+now_date)
                print (e)
            time.sleep(60)
        #没到时间判断教室目录是否存在，不存在就新建
        for classroom in dit_list.keys():
            # shutil.rmtree(classroom)
            # print(base_dir+'\\'+classroom )

            mk_dir(base_dir + '\\' + classroom)
            print(base_dir + '\\' + classroom)
            acl_dir(classroom, dit_list[classroom])

        time.sleep(2)