# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


import os
import requests
import requesocks
'''
author:qiweb
date:2018-09-01
description:利用 tor+selenium+python27+
Product Keys - My Visual Studio
url:https://my.visualstudio.com/productkeys
hlep：
pip install -r requirements.txt

requesocks==0.10.8
requests==2.19.1
selenium==2.53.6
Flask==1.0.2
Flask-API==1.0
Flask-HTTPAuth==3.2.4
Flask-RESTful==0.3.6

'''

# class UntitledTestCase(unittest.TestCase):
class UntitledTestCase():

    ###########################
    '''
    获取代理ip
    验证ip是不是可以用
    排除重复ip
    自动远程刷新ip
    '''



    # 这个是vps上的服务专门刷新ip用
    refushIPurl = "http://xxxx/xxxx"

    # 通过接口刷新tor换ip
    def refushIP(self):
        r = requests.get(self.refushIPurl)  # get请求就执行刷新
        print "ip切换成功"

    # 通过代理获取ip地址
    url = 'https://api.ipify.org?format=json'

    #代理地址14.63.227.176:9050
    torip="14.63.227.176"
    torport = "9050"
    def getip(self,url):
        print "(+) Sending request with requesocks..."
        session = requesocks.session()
        session.proxies = {'http': 'socks5://%s:%s'%(self.torip,self.torport),
                           'https': 'socks5://%s:%s'%(self.torip,self.torport)}
        r = session.get(url)
        print "(+) IP is: " + r.text.replace("\n", "")
        return r.text.replace("\n", "")

    # 保存ip
    def saveip(self,ip):
        f = open('ips.txt', 'a+')
        f.write(ip)
        f.close()

    # 判断ip是不是存在
    def exitIp(self,ip):
        ips = ''
        f = open('ips.txt', 'a+')
        ips = f.read()
        f.close()
        return ip in ips

    # 验证ip地址是不是可以用2
    def checkIp2(self):
        ip2 = ''
        i1 = 0
        while True:

            ip = self.getip(self.url)
            print i1, ip, ip2

            if ip2 == ip:
                if i1 > 3:  # 一共验证5次
                    # 保存ip
                    self.saveip(self,ip)
                    break

            else:
                i1 = 0
                ip2 = ip
            i1 = i1 + 1
        print u'可以ip为%s' % ip2
        return ip2

    ############################



    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://my.visualstudio.com/productkeys"
        self.verificationErrors = []
        self.accept_next_alert = True

    #保存账号的记事本
    qiwebEmaillist='qiwebEmaillist.txt'
    #保存已经处理过的账号
    qiwebEmaillistAlreadyhandled='qiwebEmaillistAlreadyhandled.txt'
    # 保存账号的记事本
    qiwebkeyConfig = 'qiwebkeyConfig.txt'

    #togheetxrlmi@outlook.com----vEpjC7KbqeXz
    email='togheetxrlmi@outlook.com'
    password='vEpjC7KbqeXz'
    def getEmail(self):
        i=0
        f2 = open(self.qiwebEmaillistAlreadyhandled, 'a+')
        qiwebEmaillist=f2.read()
        f2.close()

        f = open(self.qiwebEmaillist, 'a+')
        emails = f.readlines()
        f.close()
        if len(emails)==0:
            print u'没有发现待提取的账号，请在qiwebEmaillist.txt文件录入例如togheetxrlmi@outlook.com----vEpjC7KbqeXz一行一个'
            return False
        for email in emails:
            listuserandpasswrod=email.split('----')
            if len(listuserandpasswrod)==2 and (email not in qiwebEmaillist):
                self.email=listuserandpasswrod[0]
                self.password = listuserandpasswrod[1]
                i=1
                print u'当前的新账号：%s' % email
                break
            else:
                print u'已经提前过的账号：%s'%email
        if i==0:
            print u'文件qiwebEmaillist.txt中的账号都提取过了'
            return False
        return True

    def updateEmail(self):
        f2 = open(self.qiwebEmaillistAlreadyhandled, 'a+')
        f2.writelines('%s----%s----%s'%(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),self.email,self.password))
        f2.close()
        print u'保存提取过的账号成功'


    #开始提取
    def getKeyCode(self):
        driver = self.driver
        driver.get("https://my.visualstudio.com/productkeys")
        # driver.find_element_by_xpath("//form[@id='i0281']/div/div").click()
        driver.find_element_by_id("i0116").click()
        driver.find_element_by_id("i0116").send_keys(self.email)#"roastinomlm@outlook.com")
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(4)
        driver.find_element_by_id("i0118").click()
        driver.find_element_by_id("i0118").send_keys(self.password)#"61nG55hAvs2q")
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(3)
        print '5 ...'
        self.updateEmail()
        self.tearDown()
        #driver.find_element_by_id("idSIButton9").click()
        #time.sleep(5)
        # 设置国家和地区第一次登录会用到
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='我们还需要一些详细信息'])[1]/following::form[1]").click()
        # driver.find_element_by_id("create-profile-submit-btn").click()
        # 刷新
        # driver.get("file:///D:/python_dome/outlook/Product Keys - My Visual Studio.htm")

        try:
            driver.refresh()  # 刷新方法 refresh
            print ('test pass: refresh successful')
        except Exception as e:
            print ("Exception found", format(e))

        #time.sleep(5)
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Windows 10 Pro'])[13]/following::a[1]").click()

        time.sleep(10)
        print '20 ...exit'

    # 这里是总入口
    def test_untitled_test_case(self):


        #5、开始提取号码
        self.getKeyCode()



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    myclasse=UntitledTestCase()
    print "Running qiweb aout get windows  and office key ..Start."
    while myclasse.getEmail():
        # 1\  获取当前账号
        # 2、从圆球获取可以用的ip代理 经过筛选是稳定的号
        #ip = myclasse.checkIp2()
        # 3、判断这个ip之前是否有用过，如果用过，远程vps换ip
        #if myclasse.exitIp(ip):
        #   print u"ip 存在 刷新iping"
        #   myclasse.refushIP()
        #打开浏览器登录和提取
        #unittest.main()
        myclasse.setUp()
        myclasse.getKeyCode()