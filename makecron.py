import os
import requests
from string import Template
from crontzconvert import convert as convert_cron

crontab_URL = "https://github.com/VidocqH/jd_scripts/raw/master/docker/crontab_list.sh"
r = requests.get(crontab_URL)
rarr = r.text.splitlines()

'''
res中的元素示例:
['东东超市', '11 0-15,17-23/5 * * *', 'node /scripts/jd_superMarket.js']
'''
res = []
count = 0
for i in rarr[5:]:
    # 无用行
    if "#短期活动#" in i or "#长期活动#" in i or i == '':
        continue
    # 处理>>符号
    idx = i.find(">")
    if idx == -1:
        idx = len(i)
    i = i[:idx]
    if "node" in i:
        # crontab行
        i = i.rstrip()
        iarr = i.split(" ")
        # Normalize GMT+8 to GMT+0
        # 0-4元素为cron
        # 5-6元素为脚本执行命令
        cron = ' '.join(iarr[:5])
        comm = ' '.join(iarr[5:])
        cron = convert_cron(cron, 'Asia/Shanghai', 'Europe/London') # cron时区转换: https://github.com/VidocqH/cron-timezone-convert
        res[count].append(cron)
        res[count].append(comm)
        count += 1
    else:
        # action名字行
        name = i[1:].strip()
        res.append([name])
# print(res)
# exit()

'''
crondic中的元素示例:
{
    'nameCN': '京喜工厂',
    'nameEN': 'dreamFactory',
    'cron': '20 * * * *',
    'comm': 'node jd_dreamFactory.js',
    'fileName': 'jd_dreamFactory',
    'actionName': 'jd_dreamFactory_惊喜工厂'
}
'''
# convert array to dict
crondic = []
for i in res:
    if i[0] == "签到": # 懒得处理的特别情况
        crondic.append({
            'nameCN': i[0],
            'nameEN': 'bean_sign',
            'cron': i[1],
            'comm': 'node jd_bean_sign.js',
            'fileName': 'jd_bean_sign',
            'actionName': 'jd_bean_sign_签到'
        })
    else:
        if i[1][0] == '#': # 上游中此条cron被注释, 如jd_family
            continue
        crondic.append({
            'nameCN': i[0],
            'nameEN': i[2][i[2].rfind('/')+4:len(i[2])-3],
            'cron': i[1],
            'comm': 'node ' + i[2][i[2].rfind('/')+1:], # node xxx.js
            'fileName': i[2][i[2].rfind('/')+1:len(i[2])-3], # 无拓展名的文件名
            'actionName': i[2][i[2].rfind('/')+1:len(i[2])-3] + '_' + i[0]
        })
# print(crondic)
# exit()

with open('./template.txt', 'r') as f:
    template = Template(f.read())

for i in crondic:
    ymlPath = './.github/workflows/' + i['fileName'] + '.yml'
    with open(ymlPath, 'w') as f:
        f.write(template.safe_substitute(i))
