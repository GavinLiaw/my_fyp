import re
import requests

count  = 1 

url = 'website'

res = requests.get()

open('video.mp4','wb').write(res)

#这4行代码 ， 找到视频网址 就可以下载下来

#如果很多个视频网址 

#去请求个人的主页， 主页里面找到ta的这些视频的链接

#带入以上四行代码 把视频一起下载

import requests

主页 = 'https://www.douyin.com/'

#请求主页 , 然后解码数据 
伪装 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'cookie':'https://www.douyin.com/',
        'referer':''
       }

res = requests.get(主页, header = 伪装)

print(res.status_code)

import urllib


影片 = urllib.parse.unquote(res.text)

print (影片)

笑死 = re.findall('","playAddr":\[{"src}:"(.*?)"},{"src":"', 
影片)

print (笑死)

#把链接一个一个去请求
for u in 笑死 :
  下载链接 = 'https:' + u 

  res = requests.get(下载链接)

  open(f'{count}.mp4', 'wb').write(res.content)

  count += 1

  #网页 有动态加载 跟 翻页 
  # 翻页 第一页 和 第n页 是由规律的
#动态加载 = 几个人搬东西 （ 一直把东西搬上来 直到数据说明没有) 
print(影片)

has_more = re.findall(',"post":{"statusCode":0,"hasMore":(.*?),"cursor":', 影片)

id = 主页.split('/')[-1]

max_cursor = re.findall('."maxCursor":(.*?),"logPd":', 影片) #maxcursor 也是一个列表

if has_more =='1': #has more 是 一个 列表
  下一页的链接 = f'' #f是format的意思

res = requests.get(下一页的链接)

print(res.status_code)
print(res.text)

while True:
  if has_more =='1':
    JSON = requests.get(下一页的链接 , header = 伪装 )
    链接列表 = JSON['aweme_list']
    for 链接 in 链接列表:
      res = requests.get(下载链接)
      open(f'视频/{count}.mp4','wb').write(res.content)
      print(f'正在下载')
      count +=1 

      has_more = str(JSON['has_more'])
      if has_more == '0':
        break
      max_cursor = JSON['max_cursor']
      print(max_cursor)

print(下一页的链接)



