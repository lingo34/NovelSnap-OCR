import os
import ocr
import config as configFile

config = configFile.general_config


# ----- Tools ----- #


# ! 未完成
def writeFile(text):
    print("@dev正在写入文件...")
    print(text)


#
def shell(cmd):
    """run shell command, print and return the output"""
    print(os.popen(cmd).read())


# ------------------ #


def main():
    print("歡迎使用python 版NovelSnap OCR")
    screenshotOCRLoop()


# ! 未完成
# take a screenshot and do OCR
def screenshotOCRLoop(fileName="screen"):
    imgPath = getScreenshot(fileName + ".png")
    text = ocr.ocr(imgPath)
    writeFile(text)




def getScreenshot(fileName="screen.png"):
    ''' capture screen on phone using adb, pull it to local,
        clean the screenshot on phone, and return the path of the screenshot.
    Args:
        fileName: the name of the screenshot file, default is "screen.png"
    Returns:
        the path of the screenshot
    '''

    print("@dev正在截图...")
    shell("adb shell screencap -p " + config["cache_location_android"] + "/" + fileName)
    shell(
        "adb pull "
        + config["cache_location_android"]
        + "/"
        + fileName
        + " "
        + config["cache_location_pc"]
        + "/"
        + fileName
    )
    shell("adb shell rm " + config["cache_location_android"] + "/" + fileName)
    print("@dev截图完成, 图片已缓存到" + config["cache_location_pc"] + "/" + fileName)
    return config["cache_location_pc"] + "/" + fileName
