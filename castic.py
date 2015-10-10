#!/usr/bin/env python
# coding: UTF-8
# @Date    : 2015-09-16 15:46:47
# @Author  : LinPan
# @Email   : yidiyu0507@gmail.com
# @Version : 1.0

'''
Problem: 

Solution: lxml,css selector,Python:


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
'''

import requests,sqlite3
import smtplib
import sys

from  lxml import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

link='http://www.casitc.com/casitc/?cat=6'

def getinfo(link):
	
	page=requests.get(link)
	tree = html.fromstring(page.text)
	linktitle=tree.xpath('//li[contains(@style,"margin:20px")]/a/text()')
	linkhref=tree.xpath('//li[contains(@style,"margin:20px")]/a/@href')
	n=dict(zip(linkhref,linktitle))
	return n
 #避免多次插入，否则出错了！

def Sendemail(text):
	port=25
	mailto=['yidiyu0507s@163.com']
	mail_host='smtp.163.com'
	mail_user='yidiyu0507s@163.com'
	mail_pass='s1108057'
	mail_fix='163.com'
	receiver='18610710105@163.com'
	msg = MIMEText(text,_subtype='html',_charset='gb2312')
	msg['subject']='www.casitc.com'
	msg['from']=mail_user
	msg['to']=receiver

	sen=smtplib.SMTP(mail_host,port)
	sen.login(mail_user,mail_pass)
	sen.sendmail(mail_user,receiver, msg.as_string())
	sen.close()



if __name__=='__main__':
	s=''
	for index,k,v in enumerate(getinfo(link).items()):
		 #print k,v
		 boby='<br><a href='+k +'> '+ v +'</a></br>'
		 s += boby
	Sendemail(s)
	print '你的邮件已发生完毕！请查收'







#def get_con():
	conn = sqlite3.connect("F:/est.db")
	cu=conn.cursor()
	#cu.execute("create table aaa(id INTEGER PRIMARY KEY AUTOINCREMENT,title varchar(40) UNIQUE,link varchar(20), updatetime TEXT)")
	link='http://www.casitc.com/casitc/?cat=6'
	c=getinfo(link)

	save_sql = 'INSERT INTO aaa values (?, ?, ?, ?)'
	#for i in xrange(len(c)):

	#	link=c.items()[i][0]
	#	title=c.items()[i][1]
	#	date=title.split(' ')[-1]

		#cu.execute(save_sql, (None,title,link,date))
	#	conn.commit()
	#cu.execute("select * from aaa")
	#print cu.fetchone().encode('utf-8')


#	V=get_con()
