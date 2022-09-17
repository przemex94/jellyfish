#!/usr/bin/env python3
from selenium import webdriver
print("   _      _ _        __ _      _     ")
print("  (_)    | | |      / _(_)    | |    ")
print("   _  ___| | |_   _| |_ _  ___| |__  ")
print("  | |/ _ \ | | | | |  _| |/ __| '_ \ ")
print("  | |  __/ | | |_| | | | |\__ \ | | |")
print("  | |\___|_|_|\__  |_| |_||___/_| |_|")
print(" _/ |          __/ |                 ")
print("|__/          |___/                  ")
print("-------------------------------------")
print(" jellyfish.py - Clickjacking checker.")
print(" Copyright (c) ING Hubs Poland       ")
print(" przemyslaw.aniol@ing.com            ")
print("-------------------------------------")
print("                                     ")                                         
print("          ▒▒▒▒▒▒▒▒▒▒                 ")                  
print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒               ")                  
print("      ▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒             ")                  
print("      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             ")                  
print("      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             ")                  
print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒               ")                  
print("        ▒▒  ▒▒  ▒▒  ▒▒               ")                  
print("      ▒▒▒▒  ▒▒  ▒▒  ▒▒               ")                  
print("      ▒▒  ▒▒  ▒▒  ▒▒  ▒▒             ")                  
print("      ▒▒  ▒▒  ▒▒  ▒▒  ▒▒             ")                  
print("        ▒▒  ▒▒▒▒▒▒  ▒▒               ")                  
print("        ▒▒  ▒▒  ▒▒  ▒▒               ")                  
print("                                     ")
print("                                     ")
print("                                     ")
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
    driver.get("file:///C:/Users/OO42GR/OneDrive%20-%20ING/Desktop/jellyfish/jellyfish.html")
    driver.switch_to.frame('clickframe')
    result = driver.page_source.__contains__("refused to connect.")
    if result == 1:
        pass
    else:
        print(line.strip()+" "+"-"+" ""clickjacked!")
    driver.close()
driver.quit()
