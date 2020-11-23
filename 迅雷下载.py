# -*- coding: utf-8 -*-

# @project :xunlei_download
# @File    : 迅雷下载.py
# @Date    : 2020-11-23-16
# @Author  : XRL

import os
import time
import pyautogui
import base64
import re

'''
在任意地址创建文本文档，名称自定义，例如：C:\\Users\\xxx\\Desktop\\迅雷下载地址.txt
文本文档中的链接可以是迅雷链接或其他本地下载链接，包括ftp链接
执行后根据固定路径的文本文档中的地址开始下载，下载保存目录需要在迅雷软件中自行设置
每2分钟检查一次是否全部下载完成
'''
save_path = 'D:\\迅雷下载\\'

def geturl():#从文本文档中获取下载链接列表
    with open('C:\\Users\\xxx\\Desktop\\迅雷下载地址.txt','r',encoding='utf8') as f:
        linklist = f.readlines()
    return linklist

def thunder_2_normal(url:str):#迅雷链接转换成普通下载链接
    urla = url.lstrip('thunder://')
    urlb = base64.b64decode(urla).decode('utf8')
    urlb = urlb.strip('AAZZ')
    return urlb

def get_filename(link):#从下载链接中获取文件名，如果是迅雷链接，则还原成普通链接
    find_name = re.compile(r"[^/]+$")
    if 'thunder://' in link:
        link = thunder_2_normal(link)
        filename = re.findall(find_name,link)
        return filename
    else:
        filename = re.findall(find_name,link)
        return filename

def check(filename):#检查文件是否下载完成
    return os.path.exists(os.path.join(save_path,filename))#True/False

def download(link):#根据下载地址列表下载（下载目录为迅雷中设置的目录）

    os.system('"C:\Program Files (x86)\Thunder\Program\ThunderStart.exe" {url}'.format(url=link))
    pyautogui.press('enter')
    time.sleep(0.5)
    print('正在下载')
    name = get_filename(link)
    while True:
        time.sleep(120)
        if check(name):
            return True

def main():#主程序，
    print('下载开始前不要操作')
    urllist = geturl()
    for url in urllist:
        if download(url):
            print('=======下载完成========')
        else:
            print('=======下载中========')

if __name__ == '__main__':
    print('地址存放路径为 C:\\Users\\xxx\\Desktop\\迅雷下载地址.txt')
    main()