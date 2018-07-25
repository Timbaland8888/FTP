# coding=utf-8
# import Tkinter
# import tkMessageBox
#
#
# def show():
#     tkMessageBox.showinfo(title='何老师温馨提示您', message='上传作业前，请手动清空上一位同学的作业！！！')
#
#
# def creatfram():
#     root = Tkinter.Tk()
#     b = Tkinter.Button(root, text="开始上传作业", command=show)
#     b.pack()
#     root.mainloop()
#
#
# creatfram()
#
# import Tkinter
# import tkMessageBox
#
# top = Tkinter.Tk()
# top.withdraw()
# tkMessageBox.showinfo(title='何老师温馨提示您', message='上传作业前，请手动清空上一位同学的作业！！！')
import re
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
import os,shutil,datetime
now_date = datetime.datetime.now().strftime('%M-%S')
sharedir= 'D:\\'
os.chdir(sharedir)
print os.listdir(sharedir)
for f in os.listdir(sharedir):
    try:
        # time.sleep(1)
        if re.findall('A01', f) == ['A01']:
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s"  ' % (f))
        elif re.findall('B01', f) == ['B01']:
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s"  ' % (f))
        elif re.findall('C01', f) == ['C01']:
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s"  ' % (f))
        elif re.findall('D01', f) == ['D01']:
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s"  ' % (f))
        elif re.findall('E01', f) == ['E01']:
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s"  ' % (f))
        elif re.findall('teacher', f) == ['teacher']:
            del_dir = 'D:\\teacher'
            os.chdir('D:\\teacher')
            # 递归不询问删除目录及文件
            os.popen('rmdir /s/q "%s\\1403"  ' % (del_dir))
            os.popen('rmdir /s/q "%s\\1404"  ' % (del_dir))
            os.popen('rmdir /s/q "%s\\1405"  ' % (del_dir))
            os.popen('rmdir /s/q "%s\\1406"  ' % (del_dir))
            os.popen('rmdir /s/q "%s\\1407"  ' % (del_dir))
        else:
            print "don't delete  files "
    except Exception,e:
            # print unicode(now_date+str(f),'utf-8')
            # print os.rename(f,f+now_date)
            print e


