import re
import requests

url = 'https://www.youtube.com/s/search/audio/success.mp3' #找playurl？ (播放连接)

res = requests.get(url)

open('youtube.mp3', 'wb').write(res.content)

#找到音乐的链接 https://xxxx.mp3 下载这个音乐

#2. 这些音乐的链接在playUrl (播放链接) 里面

# 注意: https://xxxxx?xxx=xxxx&xxx （类似这样 https://u.jd.com/GuHUWuj?sn=hh）

#mid 是 music id
#type=music 是 类型音乐
#httpsStatus=1 是 网页状态
#reqId = xxxx-xxxx 是验证码 

import requests

url = 'https://kuwo.cn/api/www/search/searchKey?key=&httpsStatus=1&reqId=e15578b0-fbb9-11ed-a505-1f2ff81a7cfa'

#伪装
wz = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'kw_token=64UU6EF6768',
    'csrf': '64UU6EF6768',
    'Host':'kuwo.cn',
    'Referer': 'https://kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1'}

res = requests.get(url)

print(res.text)

编号 = re.findall(',"rid":(.*?),"duration":',res.text)
regID = re.findall('"reqId":"(.*?)","tId"',res.text)[0]
歌曲名 - re.findall('"name":"(.*?)","online":',res.text)

print(编号)
print(regID)

for id in range(len(编号)):
    播放链接 = f'https://kuwo.cn/api/www/search/searchKey?key=&httpsStatus=1&reqId=e15578b0-fbb9-11ed-a505-1f2ff81a7cfa'

    res = requests.get(播放链接)
    mp3_url = re.findall('url":"(.*?)","profileID"',res.text)[-1]

    #请求播放链接:
    res = requests.get(mp3_url, headers = wz)
    open(f'xxx.mp3','wb').write(res.content) #歌手 歌曲 编号.mp3

#逻辑
#列表可以同时存放多个数据
name = ['x1','232','hello','爱','@wefe比']
print(name)

#索引 (左往右 0开始， 右往左 -1开始)
print(name[1])
print(name[-4])
#0,1，2，3，4
#-5,-4,-3,-2,-1

#遍历列表中的每一个元素
#for n in name:   #'x1','232','hello','爱','@wefe比'