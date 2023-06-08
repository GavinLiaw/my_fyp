#how to find video url
#1. 在浏览器右上角菜单--更多工具--开发者工具
#2. 选中network， 选中media
#3. 浏览器左上角点击刷新 看见1-3条数据
#4. 点击 一条数据 选general request url

url = "https://www.youtube.com/s/search/audio/failure.mp3"

#用url scrap里面数据
#请求模块 - request
#1. 导入请求代码
#2. 使用模块 
# 运行提示: No module named requests 没有找到运行模块! 解决方案：pip install request ( if use pycharm)
#使用模块 （奶茶 = 手机.付款(20块钱)）人话就是 手机是工具 有一个付款功能 给20块钱 得到奶茶
#使用模块 (美女 = 手机.拍照(20块钱)) 人话就是 手机是工具 有一个拍照功能 给20块钱 得到美女
#requests 是一个模块（工具） 有一个get功能 给一个url 得到网址的相应res

import requests 
# 响应 = 工具.功能(工作)
res = requests.get(url)

#响应res 是什么东西？不是一个东西！ 很多个东西!
#比如姓名 年龄 身高 体重 肉体 灵魂 女友

res.status_code #响应码： 200 （成功） ， 403（拒绝）， 404（丢失), 500（错误）

print(res.status_code)

res.content #响应的内容 (得到的视频数据)

#把内容保存到电脑上
#打开文件 open("文件名","打开方式")

open("test.mp4","wb").write(res.content) #打开方式, 打开之后指挥写 ，写什么？ 写res里面的东西

#把res content 放进去新开的文件 
#然后读(read)跟写(write)数据 
#文本(txt)文件 还是 二进制文件(mp3,mp4,avi,jpeg,exe,xlsx,ppt)
#rb(read-binary) wb(write-binary)



