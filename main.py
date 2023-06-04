import os
from paddleocr import PaddleOCR





def main():
    print("歡迎使用python 版NovelSnap OCR")
    screenshotOCRLoop()



# ! 未完成
# take a screenshot and do OCR
def screenshotOCRLoop():
    imgPath = captureScreen()
    text = ocr(imgPath)
    writeFile(text)







# ! 未完成
def captureScreen(fileName = "screen.png"):
    print("@dev正在截图...")
    return './cache/screen.png'

# ! 未完成
def writeFile(text):
    print("@dev正在写入文件...")
    print(text)

def adb_shell(cmd):
    exit_code = os.system(cmd)
    return exit_code>>8
    # # os.system(cmd)命令会直接把结果输出，所以在不对状态码进行分析处理的情况下，一般直接调用即可
    # os.system(cmd)

