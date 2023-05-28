# NovelSnap-OCR
A node.js script to extract novels from android novel apps using OCR and ADB
一个使用 OCR 和 ADB 从安卓小说应用中提取小说的 Node.js 脚本

Not done yet, check back later
本程序尚未完成开发(资料夹已创建), 晚点再回来吧

目前状态: 因为tesseract-OCR库效果实在不太行, 正在考虑换ocr库, 但是由于支持node 的本地ocr库好像不太多, 目前正在考虑切到python去写, 但是由于我并不会写python, 所以正在考虑去学个python😂

# Goal
目标是留存互联网上因为过于先进的反爬虫机制, 导致难以获取的小说资源。
起因是我今日想起了多年以前看的一部小说, 结果发现下架了, 网络上也没有数字留存。
就让人忍不住想做点什么, 保留一下珍贵的资源。
另外有些小说网页的反爬虫机制十分先进, 愚蠢如我也只能想到adb操控手机 + ocr文字识别的笨方法了。



# Steps
0. adb 连接
1. 获取截图 (adb截图, 传输截图到电脑, 删除android中的截图)
4. ocr 提取文字 并储存
5. 删除电脑上的截图缓存
6. 翻页
---

# 要求 requirements
- adb
- node.js
- 安装好并能正常使用的tesseract

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


# 使用的库
- [node-tesseract-ocr](https://www.npmjs.com/package/node-tesseract-ocr), MIT License

- [prompt-sync](https://www.npmjs.com/package/prompt-sync), MIT License
- [shelljs](https://www.npmjs.com/package/shelljs), BSD-3-Clause

