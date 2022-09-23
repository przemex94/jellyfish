#!/bin/bash
dpkg -i ./src/chrome.deb
cp ./src/chromedriver /bin/chromedriver
pip3 install selenium
