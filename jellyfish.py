#!/usr/bin/env python3
from selenium import webdriver
print("-------------------------------------")
print(" jellyfish.py - Clickjacking checker.")
print(" Copyright (c) ING Hubs Poland       ")
print(" przemyslaw.aniol@ing.com            ")
print("-------------------------------------")
print("  =====D                             ")
print("                        =====D       ")
print("         =====D                      ")
print("-------------------------------------")
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
    driver = webdriver.Chrome()
    driver.get("file:///opt/jellyfish/jellyfish.html")
    driver.switch_to.frame('clickframe')
    result = driver.page_source.__contains__("refused to connect.")
    if result == 1:
        pass
    else:
        print(line.strip()+" "+"-"+" ""clickjacked!")
    driver.close()
driver.quit()
