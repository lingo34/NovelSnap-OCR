from cnocr import CnOcr

# ! doing
# def ocr(imgPath, lang="ch"):
#    print("OCR")
#    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
#    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
#    ocr = PaddleOCR(use_angle_cls=True, lang=lang)  # need to run only once to download and load model into memory
   
#    result = ocr.ocr(imgPath, cls=True)
#    for index in range(len(result)):
#        res = result[index]
#        for line in res:
#            print(line + "^")

img_fp = './cap.png'
ocr = CnOcr()  # 所有参数都使用默认值
out = ocr.ocr(img_fp)

print(out)




# ocr("./cache/screen.png")




