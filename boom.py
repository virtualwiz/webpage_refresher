# -*- coding=utf-8 -*- 
import urllib2
import socket
import time

#urls = raw_input("Please enter a web address: \n> ")
print "\nAccess web page start..."
i = 0
while 1:
    url = 'http://jwc.wit.edu.cn/news/newsInfo.do?id=-1&&articleid=1130'
    socket.setdefaulttimeout
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip',
    'Connection':'close',
    'Referer':None 
    }
    req_timeout = 600
    req = urllib2.Request(url,None,req_header)
    print "Phase 1:  Transmitting Request"
    resp = urllib2.urlopen(req,None,req_timeout)
    print "Phase 2:  Receiving"
    html = resp.read()
    #print html
    print "Phase 3:  Cooling down ",i
    i = i + 1
    time.sleep(0)
