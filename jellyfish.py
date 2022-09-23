#!/usr/bin/python3 
from selenium import webdriver
print("--------------------------------------------")
print("jellyfish.py - Clickjacking checker.        ")
print("przemex94 - przemyslaw.aniol@protonmail.com ")
print("--------------------------------------------")
print("     =====D                                 ")
print("                              =====D        ")
print("               =====D                       ")
print("--------------------------------------------")
file = open('jellyfish.txt', 'r')
lines = file.readlines()
i = 0
for line in lines:
    i += 1
    URL = line
    html = '''
    <html>
    <body>
    <iframe  id="clickframe" name="clickframe" src="'''+URL+'''" height='600px' width='800px'></iframe>
    </body>
    </html>'''
    html_file = 'jellyfish.html'
    f = open(html_file, 'w+')
    f.write(html)
    f.close()

    first = webdriver.Chrome()
    first.get(URL)
    firstresult = first.page_source.__contains__("refused to connect.")
    
    second = webdriver.Chrome()
    second.get("file:///opt/jellyfish/jellyfish.html")
    second.switch_to.frame('clickframe')
    secondresult = second.page_source.__contains__("refused to connect.")

    if ((firstresult != secondresult) and (secondresult == 1)):
        pass
    else:
        print(line.strip()+" "+"-"+" ""CLICKJACKED!")
    first.close()
    second.close()
first.quit()
second.quit()
