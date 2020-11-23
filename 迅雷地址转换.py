# -*- coding: utf-8 -*-

# @project :xunlei_download
# @File    : 迅雷地址转换.py
# @Date    : 2020-11-23-16
# @Author  : XRL


import base64

def normal_2_thunder(url:str):
    urla = url
    urla = 'AA'+urla+'ZZ'
    urla = urla.encode('utf8')
    urlb = base64.b64encode(urla).decode('utf8')
    urlb = 'thunder://'+urlb
    print(urlb)

def thunder_2_normal(url:str):
    urla = url.lstrip('thunder://')
    urlb = base64.b64decode(urla).decode('utf8')
    urlb = urlb.strip('AAZZ')
    print(urlb)

def main(url):
    if 'thunder://' in url:
        thunder_2_normal(url)
    else:
        normal_2_thunder(url)

if __name__ == '__main__':
    main(input("请输入地址"))
