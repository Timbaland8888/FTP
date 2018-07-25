#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#Arthor:Timbaland
#date:20180124
import os,sys
import Tkinter
import tkMessageBox
def net_disk(host,shardir):
    cmd = r"start \\%s%s " %(host,shardir)
    print cmd
    os.popen(cmd)
    return True
if __name__ == '__main__':
     f =os.popen('whoami').read()
     host = 'FTP'
     shardir ='\\'+f.split('\\')[1]
     top = Tkinter.Tk()
     top.withdraw()
     tkMessageBox.showinfo(title='何老师温馨提示您', message='上传作业前，请手动清空上一位同学的作业，谢谢配合！！')
     net_disk(host=host,shardir=shardir)
