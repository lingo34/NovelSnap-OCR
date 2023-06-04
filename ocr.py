from cnocr import CnOcr
import config
import numpy as np


ocr_config = config.ocr_config


def ocr(imgPath) -> list:
    """
    OCR the image and return the text
    Args:
        imgPath: path of the image to be recognized

    Returns:
        text: the text recognized from the image
    """
    # see CnOCR documentation https://cnocr.readthedocs.io/zh/latest/usage/#_4
    ocr = CnOcr(
        rec_model_name=ocr_config["rec_model_name"], rec_root=ocr_config["rec_root"]
    )
    # see CnOCR documentation https://cnocr.readthedocs.io/zh/latest/usage/#1-cnocrocrimg_fp
    resultList = ocr.ocr(
        imgPath,
        resized_shape=ocr_config["resized_shape"],
        min_box_size=ocr_config["min_box_size"],
    )
    print(resultList)
    return toText(resultList)


def toText(
    ocrList,
    top_ignore=ocr_config["top_ignore"],
    bottom_ignore=ocr_config["bottom_ignore"],
):
    """convert the result of ocr (list with position and accuracy) to text
    Args:
        ocrList: the raw result of ocr in a list
        top_ignore: ignore the result on the top x pixels of the image
        bottom_ignore: ignore the result on the bottom x pixels of the image
    Returns:
        text: properly formatted text as the result of ocr
    """
    text = ""
    for result in ocrList:
        y = int(result["position"][0][1])

        if y <= top_ignore or y >= (ocr_config["resized_shape"][0] - bottom_ignore):
            # print("忽略:")
            # print(result)
            # print("理由: " + str(y <= top_ignore) + " || ")
            continue
        text += "".join(result["text"])
    return text


# print(ocr("./cache/cap.png"))

# ocr("./cache/screen.png")
