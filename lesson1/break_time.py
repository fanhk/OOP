__author__ = 'fhk'
import webbrowser
import time

total_breaks = 3
count_break = 0

print "This program begin at " + time.ctime()
while count_break < total_breaks:
    time.sleep(10)
    webbrowser.open("www.baidu.com")
    count_break += 1
