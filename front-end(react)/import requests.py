#爬虫必备
import requests
url = 'https://live.douyin.com/webcast/ranklist/audience/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=en-US&enter_from=web_live&cookie_enabled=true&screen_width=694&screen_height=763&browser_language=en-US&browser_platform=Win32&browser_name=Chrome&browser_version=113.0.0.0&webcast_sdk_version=2450&room_id=7237057805872646968&anchor_id=65046766481&sec_anchor_id=MS4wLjABAAAAqoyHWSa28DI1dG8NFjbBWRjoj3uxdqEwrV1SGJeCVSo&rank_type=30&msToken=1bykkcyPaXdIbRFaVZsOBFz-qRKotZRaZbi_rFJ__p9Hrw5r6OYMr2xxFTI7aJED00kfyMCzR02N4IW0RVaCbc5py2TVYuE2dtwSYSdcVyhTU_9LYRlkm-ecblwzE648&X-Bogus=DFSzswVOkUiANxKfttmQuXoBpDi3&_signature=_02B4Z6wo000011orNLgAAIDBSnSmauCtKAtaKzAAALLwsiedfTbufPSIgNk3otK4M0co1pO6zPYP6y5KQCY.6TXvoYCdtuPn7dzgu3p0zpJr.oNiohE3awVPEPlmjyMbxSdGjsUy-AfI4jbE19'
wz = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36', 
      'cookie':'passport_assist_user=CjzNEytfqboB9CbiqbXGTWhIDif6-lclDhtr2xgoCnY8iYPjjyFDtVXArUjiMFgBSDYGnlvw8d41wGCY4mcaSAo8Sy2G64IYpzjXcZw3BoAjLRdEB5GU82CiEu05EBV41APsEVobB_0RSyE-IA4_a6Ti1TStGgOoi_JMPR8YEJPjow0Yia_WVCIBA2Bi6WM%3D; odin_tt=a8c66f43b6b52ccb8c4577deac82aff244e6cac3d1325fa2c568dbf11aeddb315e167606f5ec5ce606e62a690c2faf3a; sid_guard=0ee0db2f7f5d5a9f2d218fe4e1256a95%7C1671387892%7C4754542%7CSat%2C+11-Feb-2023+19%3A07%3A14+GMT; ttwid=1%7CZM_z73TTmbi4q-LfVAQM76ALSa1sZC_2Pqa9r4DWegE%7C1683469930%7C637b86c47bf33d359521ccc22700ecde0a40c5d6181f3c986f0f5f4ce5acac3f; passport_csrf_token=db4b36818d601414e75fce17f51ccf27; passport_csrf_token_default=db4b36818d601414e75fce17f51ccf27; SEARCH_RESULT_LIST_TYPE=%22single%22; strategyABtestKey=%221685015708.445%22; pwa2=%222%7C0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1685620957994%2C%22type%22%3A1%7D; home_can_add_dy_2_desktop=%221%22; download_guide=%223%2F20230525%22; __live_version__=%221.1.0.9614%22; device_web_cpu_core=5; device_web_memory_size=4; live_can_add_dy_2_desktop=%220%22; csrf_session_id=d05bc0ecdac407a4c44613553931c4c0; xgplayer_user_id=886504918124; __ac_nonce=0646f4e930042a06073bd; __ac_signature=_02B4Z6wo00f01D9Dh6QAAIDCLxwVdg8lJEQ.Y4MAAGvG94; webcast_local_quality=sd; webcast_leading_last_show_time=1685016210887; webcast_leading_total_show_times=1; msToken=Sty-mtvF4xI7-xpMzwAkHQc3k2cJpOTsggMDyNvbgThMcjfpDYqpoKlfKl7Kw0LEFS5YGuTSjKaBgQehUVXCLW0k63Ti0UQVwlwY5_5ldjHU78k86ojMYGLour6cAxLv; ttcid=afe04e819f3f45eea5da247adb1a9d2b21; tt_scid=yHkp.jSes3lqvk4GZn.JxThxwt.42Lln24btSOgtzs3BELdAmAVtMBtYKNTW6.CN2cc3; msToken=1bykkcyPaXdIbRFaVZsOBFz-qRKotZRaZbi_rFJ__p9Hrw5r6OYMr2xxFTI7aJED00kfyMCzR02N4IW0RVaCbc5py2TVYuE2dtwSYSdcVyhTU_9LYRlkm-ecblwzE648'} 
#浏览器版本 和 登录信息 #准备好伪装的信息
res = requests.get(url, headers=wz) #请求网址 得到相应
print(res)

#找到网址
#1. 打开直播间
#2. 打开f12
#放大镜搜索
#点开一条数据 表头
#找到链接的同时 顺带把用的浏览器的版本 和 登录信息拿一下

res.status_code #响应码 200 403 404 500
res.content     #响应码 
res.text 

print(res.text)
#从res.text 把重要的信息拿出来

import re
x = re.findall('"gender":"(.*?)"',res.text)
print(x)

for gender in x: #用gender找x
    print(gender)