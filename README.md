# NovelSnap-OCR
A python script to extract novels from android novel apps using OCR and ADB
一个使用 OCR 和 ADB 从安卓小说应用中提取小说的 python 脚本

Not done yet, check back later
本程序尚未完成开发(资料夹已创建), 晚点再回来吧

# Goal
目标是留存互联网上因为过于先进的反爬虫机制, 导致难以获取的小说资源。
起因是我今日想起了多年以前看的一部小说, 结果发现下架了, 网络上也没有数字留存。
就让人忍不住想做点什么, 保留一下珍贵的资源。
另外有些小说网页的反爬虫机制十分先进, 愚蠢如我也只能想到adb操控手机 + ocr文字识别的笨方法了。


# 使用:

## 要求 requirements
- adb
- python, 开发版本为`3.10`
- 安装好并能正常使用的tesseract

## 安装
~~~ sh
pip install -r requirements.txt
~~~
首次运行时要下载ocr模型, 可能会比较慢




# 笔记:

## Steps
0. adb 连接
1. 获取截图 (adb截图, 传输截图到电脑, 删除android中的截图)
4. ocr 提取文字 并储存
5. 删除电脑上的截图缓存
6. 翻页
---

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


# 使用的库
- [CnOCR](https://github.com/breezedeus/cnocr), Apache-2.0 license

