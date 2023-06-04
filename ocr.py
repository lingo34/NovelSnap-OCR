from cnocr import CnOcr
import config


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
        rec_model_name=ocr_config["rec_model_name"],
        rec_root=ocr_config["rec_root"]
        )
    # see CnOCR documentation https://cnocr.readthedocs.io/zh/latest/usage/#1-cnocrocrimg_fp
    return ocr.ocr(imgPath,
                   resized_shape=ocr_config["resized_shape"],)




print(ocr("./cap.png"))

# ocr("./cache/screen.png")




