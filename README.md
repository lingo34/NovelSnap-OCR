# NovelSnap-OCR
A node.js script to extract novels from android novel apps using OCR and ADB

Not done yet, check back later
本程序尚未开始开发(资料夹已创建), 晚点再回来吧


# Goal
目标是留存互联网上因为过于先进的反爬虫机制, 导致难以获取的小说资源。
起因是我今日想起了多年以前看的一部小说, 结果发现下架了, 网络上也没有数字留存。
就让人忍不住想做点什么, 保留一下珍贵的资源。
另外有些小说网页的反爬虫机制十分先进, 愚蠢如我也只能想到adb操控手机 + ocr文字识别的笨方法了。



# Steps
0. adb 连接
1. adb 截图
2. 传输截图至电脑
3. 删除android 手机中的截图
4. ocr 提取文字
5. 删除电脑上的截图缓存
6. 翻页

1. 获取截图
2. ocr 储存文字
3. 删除截图
4. 翻页

# 要求 requirements
- adb
- node.js

# 笔记:

## config.json 格式
所有档案位置末端都不加 `/`
举个例子, `/sdcard`是正确的, `/sdcard/`是错误的

## adb 命令
> 参考 [知乎](https://zhuanlan.zhihu.com/p/290670672)

~~~ sh
adb

adb shell /system/bin/screencap -p /sdcard/cap.png

adb pull /sdcard/cap.png c:\Users\Administrator\Desktop

adb shell rm /sdcard/cap.png
~~~





