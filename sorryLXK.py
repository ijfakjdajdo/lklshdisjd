# -*- coding: UTF-8 -*-
import os
import re

fileDir = "./"
fileList = []
for root, dirs, files in os.walk(fileDir):
    for fileObj in files:
        if '.git' in root or 'icon' in root:
            continue
        fileList.append(os.path.join(root, fileObj))

for fileObj in fileList:
    if 'sorryLXK' in fileObj:
        continue
    f = open(fileObj, 'r+', errors='ignore')
    lines = f.readlines()
    f.seek(0)
    # f.truncate()
    for line in lines:
        origin = 'JSON.stringify(process.env).indexOf("GITHUB")>-1'
        origin2 = "JSON.stringify(process.env).indexOf('GITHUB')>-1"
        result = '0'
        f.write(line.replace(origin, result))
    f.close()

fileDir = "./"
fileList = []
for root, dirs, files in os.walk(fileDir):
    for fileObj in files:
        if '.git' in root or 'icon' in root:
            continue
        fileList.append(os.path.join(root, fileObj))

for fileObj in fileList:
    if 'sorryLXK' in fileObj:
        continue
    f = open(fileObj, 'r+', errors='ignore')
    lines = f.readlines()
    f.seek(0)
    # f.truncate()
    for line in lines:
        origin = 'JSON.stringify(process.env).indexOf("GITHUB")>-1'
        origin2 = "JSON.stringify(process.env).indexOf('GITHUB')>-1"
        result = '0'
        f.write(line.replace(origin2, result))
    f.close()

    # sed -i s/JSON.stringify(process.env).indexOf("GITHUB")>-1/0/g `grep JSON.stringify(process.env).indexOf("GITHUB")>-1 -rl --include="*.*" ./`