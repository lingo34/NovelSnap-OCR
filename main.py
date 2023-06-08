import os
import ocr
import config as configFile

# import cv2

config = configFile.general_config


# ----- Tools ----- #


# ? 未完成
def writeFile(text, fileName="text.txt"):
    print("@dev正在写入文件...")

    # check if the output location is set and sanitize it
    if(config["text_output_location"] == ""):
        print("请在config.py中设置text_output_location")
        return
    if(config["text_output_location"].endswith("/")):
        config["text_output_location"] = config["text_output_location"][:-1]
    
    if(not os.path.exists(config["text_output_location"])):
        os.mkdir(config["text_output_location"]
                    )
    
    open(config["text_output_location"] + "/" + fileName.replace('/', ''), "w").write(text)
    print(text)
    print("@dev写入完成, 文件已保存到" + config["text_output_location"] + "/" + fileName.replace('/', ''))


#
def shell(cmd):
    """run shell command, print and return the output"""
    print(os.popen(cmd).read())


# ------------------ #


def main():
    print("歡迎使用python 版NovelSnap OCR")
    # screenshotOCRLoop()
    writeFile(ocr.ocr("./cache/screen.png"))
    print("感謝使用")


# ? 未完成
# take a screenshot and do OCR
def screenshotOCRLoop(fileName="screen"):
    imgPath = getScreenshot(fileName + ".png")
    text = ocr.ocr(imgPath)
    writeFile(text)


def getScreenshot(fileName="screen.png"):
    """capture screen on phone using adb, pull it to local,
        clean the screenshot on phone, and return the path of the screenshot.
    Args:
        fileName: the name of the screenshot file, default is "screen.png"
    Returns:
        the path of the screenshot
    """

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


main()
