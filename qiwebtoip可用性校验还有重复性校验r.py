#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
import requesocks

url = 'https://api.ipify.org?format=json'


def getip_requests(url):
    print "(+) Sending request with plain requests..."
    r = requests.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")


def getip_requesocks(url):
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://14.63.227.176:9050',
                       'https': 'socks5://14.63.227.176:9050'}
    r = session.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")

#这个是vps上的服务专门刷新ip用
refushIPurl="http://xxxx/xxxx"
#通过接口刷新tor换ip
def refushIP():
    r = requests.get(refushIPurl)#get请求就执行刷新
    print "ip切换成功"
    


#通过代理获取ip地址
url = 'https://api.ipify.org?format=json'
def getip(url):
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://14.63.227.176:9050',
                       'https': 'socks5://14.63.227.176:9050'}
    r = session.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")
    return r.text.replace("\n", "")

#保存ip
def saveip(ip):
    f = open('ips.txt','a+')
    f.write(ip)
    f.close()

#判断ip是不是存在
def exitIp(ip):
    ips=''
    f = open('ips.txt','a+')
    ips=f.read()
    f.close()
    return ip in ips

#验证ip地址是不是可以用2
def checkIp2():
    ip2=''
    i1=0
    while True:
     
        ip=getip(url)
        print i1 ,ip,ip2
                
        if ip2==ip:
            if i1>3:#一共验证5次
                #保存ip
                saveip(ip)
                break        
            
        else:
            i1=0
            ip2=ip
        i1=i1+1
    print u'可以ip为%s'%ip2
    return ip2


#验证ip地址是不是可以用
def checkIp():
    ip2=''
    i1=0
    while True:
        
        ip=getip(url)
        print i1 ,ip,ip2
        if i1==0:
            ip2=ip
        if ip2==ip and i1>4:
            break        
        if ip2==ip and i1!=0:
            i1=i1+1
            continue
        elif ip2==ip and i1==0:
            i1=i1+1
            pass
        else:
            i1=0
            continue

    print u'可以ip为%s'%ip2
    

def main():
    print "Running tests..."
    ip=checkIp2()
    if exitIp(ip):
        print u"ip 存在 刷新iping"
        refushIP()
    #getip_requests(url)
    #getip_requesocks(url)
    #os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo quit) | nc localhost 9051""")
    #getip_requesocks(url)


if __name__ == "__main__":
    main()
